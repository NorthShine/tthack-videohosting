from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

from src.config import get_config
from src.db import database
from src.schemas import Settings, UserBase
from src.blueprints.video.views import router as video_router
from src.repositories import UserRepository

base_settings = get_config()['base']

app = FastAPI(debug=base_settings['debug'], reload=True)
app.include_router(video_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@AuthJWT.load_config
def get_config():
    return Settings()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={'detail': exc.message}
    )


@app.post('/sign_in')
async def sign_in_view(user: UserBase, Authorize: AuthJWT = Depends()):
    user_repo = UserRepository(database)
    user_obj = await user_repo.get_user_by_username(user.username)
    if not user_obj or not user_repo.verify_password(user_obj.id, user.password):
        raise HTTPException(status_code=401, detail='No such user with these credentials')
    access_token = Authorize.create_access_token(subject=user.username)
    return {'access_token': access_token}
