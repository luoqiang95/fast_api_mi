from schemas import User
from fastapi import APIRouter, Depends
from virtual_data import users, user_info

from fastapi.security import OAuth2PasswordRequestForm
from handler import create_access_token, get_current_user

user_api = APIRouter(tags=["用户"], prefix="/user")


@user_api.post("/login")
async def login(user: User):
    if user.name not in users:
        return {"code": 400, "msg": "登录失败"}
    if user.pwd != users.get(user.name).get("pwd"):
        return {"code": 400, "msg": "登录失败"}
    data = {"sub": user.name}
    token = create_access_token(data=data)
    return {"code": 200, "access_token": token}


@user_api.post("/token")
async def get_token(data: OAuth2PasswordRequestForm = Depends()):
    """
    获取token
    """
    data = {"sub": data.username}
    access_token = create_access_token(data=data)
    return {"access_token": access_token}


@user_api.get("/list")
async def get_data(user: User = Depends(get_current_user), ):
    return {"code": 200, "virtual_data": user_info}



