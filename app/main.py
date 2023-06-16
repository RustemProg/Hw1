from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.auth.router import router as auth_router
from app.config import client, env, fastapi_config
from app.tweets.router import router as tweets_router
from app.shanyraks.router import router as shanyrak_router

app = FastAPI(**fastapi_config)


@app.on_event("shutdown")
def shutdown_db_client():
    client.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=env.CORS_ORIGINS,
    allow_methods=env.CORS_METHODS,
    allow_headers=env.CORS_HEADERS,
    allow_credentials=True,
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(tweets_router, prefix="/tweets", tags=["Tweets"])
app.include_router(auth_router, prefix="/shanyraks", tags=["shanyraks"])
