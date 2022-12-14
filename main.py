from api_studia.modules import (
    FastAPI,
    subprocess,
    PUBLIC_DIR,
    AuthJWTException,
    JSONResponse,
    AuthJWT,
    Request,
    StaticFiles,
    CORSMiddleware,
)
from api_studia.routes.api.kelas import kelas_route
from api_studia.routes.api.tugas import tugas_route
from api_studia.routes.api.users import user_route
from api_studia.routes.api.konten import konten_route
from api_studia.routes.api.comment import comment_route
from api_studia.routes.api.media import media_route
from api_studia.routes.api.lesson import lesson_route

from api_studia.service.auth import Setting


app = FastAPI(
    title="API Studia",
    debug=True,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.mount("/public", StaticFiles(directory=PUBLIC_DIR), name="public")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@AuthJWT.load_config
def get_config():
    return Setting()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message, "code": exc.status_code})


@app.exception_handler(403)
def forbidden_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=403, content={"message": "You are forbidden to access this page", "code": 403})


@app.exception_handler(404)
def not_found_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=404, content={"message": "Resource not found", "code": 404})


@app.exception_handler(500)
def server_error_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"message": "Server error", "code": 500})


app.include_router(kelas_route)
app.include_router(tugas_route)
app.include_router(user_route)
app.include_router(konten_route)
app.include_router(comment_route)
app.include_router(media_route)
app.include_router(lesson_route)


def start():
    cmd = ["poetry", "run", "uvicorn", "main:app", "--reload", "--host", "127.0.0.1", "--port", "8000"]
    subprocess.run(cmd, shell=True)


# c01kndoq_gzsqPZ59BBM8XPbPKmDjo9DxF9zramz7 key project
