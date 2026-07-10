from fastapi import FastAPI

from hackathon2026.api import api_router

app = FastAPI(title="Hackathon 2026 API")
app.include_router(api_router)
