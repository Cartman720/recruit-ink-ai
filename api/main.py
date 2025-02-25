from fastapi import FastAPI
from api import config
from api.lib.helpers import register_routers

app = FastAPI(title="Recruit-Ink API")

# Register all routers automatically
register_routers(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "api.main:app",
        host="127.0.0.1",
        port=config.get("PORT"),
        reload=True,
    )
