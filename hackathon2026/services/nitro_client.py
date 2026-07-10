import os
from typing import Any

import httpx

from hackathon2026.utils.env import load_project_env

MAX_ATTEMPTS = 3

# Category/cabin/price responses can take much longer than POS to compute server-side,
# so the read timeout is generous while connect/write stay short.
REQUEST_TIMEOUT = httpx.Timeout(connect=10.0, read=180.0, write=10.0, pool=10.0)


class NitroClientError(Exception):
    pass


async def post_nitro(
    path: str,
    body: dict[str, Any],
    retry: bool = True,
    timeout: httpx.Timeout | None = None,
) -> dict[str, Any]:
    # retry=False is for write calls with real side effects (charging a card, creating a
    # reservation) - retrying those on failure risks a duplicate charge/booking, since we
    # can't tell whether the first attempt actually landed server-side before it failed.
    load_project_env()
    request_timeout = timeout or REQUEST_TIMEOUT

    base_url = os.getenv("NITRO_BASE_URL", "https://localhost:44397").rstrip("/")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    site_item_id = os.getenv("SITE_ITEM_ID")

    if not client_id or not client_secret or not site_item_id:
        print("[nitro_client] missing CLIENT_ID/CLIENT_SECRET/SITE_ITEM_ID, aborting")
        raise NitroClientError("Nitro credentials are not configured.")

    url = f"{base_url}{path}"
    last_transport_error: NitroClientError | None = None
    max_attempts = MAX_ATTEMPTS if retry else 1

    for attempt in range(1, max_attempts + 1):
        print(f"[nitro_client] POST {url} body={body} (attempt {attempt}/{max_attempts})")
        try:
            # NITRO_BASE_URL is a local dev server with a self-signed cert; verification
            # is skipped only for this client, which is scoped to Nitro calls.
            async with httpx.AsyncClient(timeout=request_timeout, verify=False) as client:
                response = await client.post(
                    url,
                    json=body,
                    headers={"SiteItemId": site_item_id},
                    auth=(client_id, client_secret),
                )
                print(f"[nitro_client] received status={response.status_code}")
                response.raise_for_status()
                data = response.json()
        except httpx.HTTPStatusError as error:
            print(f"[nitro_client] HTTP error status={error.response.status_code} body={error.response.text}")
            last_transport_error = NitroClientError(f"Nitro request failed with status {error.response.status_code}.")
            continue
        except httpx.RequestError as error:
            print(f"[nitro_client] request error: {error}")
            last_transport_error = NitroClientError(f"Nitro request failed: {error}")
            continue

        if data.get("isSucceed") is False:
            print(f"[nitro_client] isSucceed=false (attempt {attempt}/{max_attempts}) response={data}")
            if attempt == max_attempts:
                return data
            continue

        return data

    raise last_transport_error
