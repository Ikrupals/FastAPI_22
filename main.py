import uvicorn
from fastapi import FastAPI

from contextlib import asynccontextmanager

from utils.database_helper import DBConnectionPool
# from api.device import device
from api.account import account
from api.application import application
from core import config

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.async_pool = DBConnectionPool()
    await app.async_pool.psyco_async_pool.open()
    yield
    await app.async_pool.close()

def get_application() -> FastAPI:
    Application = FastAPI(
        title=config.APP_NAME,
        debug=config.DEBUG,
        version=config.VERSION,
        lifespan=lifespan
    )

    # Application.include_router(device.router, prefix=config.API_PREFIX, tags=["Device"])
    Application.include_router(account.router, prefix=config.API_PREFIX, tags=["Account"])
    Application.include_router(application.router, prefix=config.API_PREFIX, tags=["Application"])
    return Application

app = get_application()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# import uvicorn
# from fastapi import FastAPI
# from contextlib import asynccontextmanager

# from utils.database_helper import DBConnectionPool
# from api.application import application
# from core import config

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     app.async_pool = DBConnectionPool()
#     await app.async_pool.psyco_async_pool.open()
#     yield
#     await app.async_pool.close()

# def get_application() -> FastAPI:
#     app = FastAPI(
#         title=config.APP_NAME,
#         debug=config.DEBUG,
#         version=config.VERSION,
#         lifespan=lifespan
#     )
#     app.include_router(application.router, prefix=config.API_PREFIX, tags=["Application"])
#     return app

# app = get_application()

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
