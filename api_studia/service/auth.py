from api_studia.modules import BaseModel, os, HTTPException, AuthJWT, Depends, JWTDecodeError
from fastapi.security.http import HTTPBearer

security = HTTPBearer()


class Setting(BaseModel):
    authjwt_secret_key: str = "ceb16b193193da3cb138a1fda5042fca203be35a5eea6a933e9717fc83ce5914"
    authjwt_access_token_expires: int = 12 * 60 * 60


def get_authorize(Authorize: AuthJWT = Depends(), Authorization: str = Depends(security)):
    try:
        Authorize.jwt_required()
    except JWTDecodeError:
        pass


def teacher_authorize(Authorize: AuthJWT = Depends()):
    role = Authorize.get_raw_jwt()
    if role["is_teacher"]:
        pass
    else:
        raise HTTPException(status_code=403)


def student_authorize(Authorize: AuthJWT = Depends()):
    role = Authorize.get_raw_jwt()
    if role["is_student"]:
        pass
    else:
        raise HTTPException(status_code=403)


def admin_authorize(Authorize: AuthJWT = Depends()):
    role = Authorize.get_raw_jwt()
    if role["is_admin"]:
        pass
    else:
        raise HTTPException(status_code=403)
