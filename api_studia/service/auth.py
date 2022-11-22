from api_studia.modules import AuthJWT, BaseModel, os, List


class Setting(BaseModel):
    authjwt_secret_key: str = os.getenv("SECRET_KEY")
    authjwt_access_token_expires: int = 216000
    authjwt_refresh_token_expires: int = 432000
    authjwt_token_location: List[str] = ["cookies"]


@AuthJWT.load_config
def get_config():
    return Setting()
