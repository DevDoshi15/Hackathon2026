from typing import Any

from hackathon2026.services.nitro_client import NitroClientError, post_nitro

TOKENIZE_CARD_PATH = "/v2/payment/TokenizeCard"

# Sandbox test cards from cruise-line-test-credit-cards.md, keyed by the POS
# pointOfSales[].apiId this booking is running through. There's no card-entry step in
# this flow yet, so a matching sandbox test card is picked automatically.
TEST_CARDS_BY_API_ID = {
    "RCCL": {"number": "4387751111111111", "type": "VI", "expiration": "12/28", "cvv": "123"},
    "NCL": {"number": "4111111111111111", "type": "VI", "expiration": "01/28", "cvv": "123"},
    "MSC": {"number": "4900000000000086", "type": "VI", "expiration": "12/28", "cvv": "123"},
    "CARNIVAL": {"number": "4035529900007013", "type": "VI", "expiration": "12/28", "cvv": "123"},
}
DEFAULT_TEST_CARD = {"number": "4111111111111111", "type": "VI", "expiration": "12/28", "cvv": "123"}

PLACEHOLDER_CARDHOLDER_NAME = "John Doe"
PLACEHOLDER_BILLING_ADDRESS = {
    "Addressline1": "123 Main St",
    "Country": {"id": "US"},
    "City": {"name": "Miami"},
}


class TokenizeService:
    async def atokenize(self, amount: float, currency: str, api_id: str | None) -> dict[str, Any]:
        card = TEST_CARDS_BY_API_ID.get((api_id or "").upper(), DEFAULT_TEST_CARD)

        body = {
            "Number": card["number"],
            "cvv": card["cvv"],
            "type": card["type"],
            "expiration": card["expiration"],
            "cardHolderName": PLACEHOLDER_CARDHOLDER_NAME,
            "amount": amount,
            "currency": currency,
            "BillingDetails": {"Address": PLACEHOLDER_BILLING_ADDRESS},
        }

        try:
            data = await post_nitro(TOKENIZE_CARD_PATH, body)
        except NitroClientError as error:
            return _tokenize_result(request=body, error=str(error))

        if not data.get("isSucceed"):
            print(f"[tokenize_service] isSucceed=false, raw={data}")
            return _tokenize_result(request=body, raw=data, error="Card tokenization did not succeed.")

        token = data.get("data", {}).get("token")
        print("[tokenize_service] success, token acquired")
        return _tokenize_result(is_succeed=True, request=body, token=token, raw=data)


def _tokenize_result(
    is_succeed: bool = False,
    token: str | None = None,
    request: dict | None = None,
    raw: dict | None = None,
    error: str | None = None,
) -> dict[str, Any]:
    return {
        "is_succeed": is_succeed,
        "token": token,
        "request": request,
        "raw": raw,
        "error": error,
    }


tokenize_service = TokenizeService()
