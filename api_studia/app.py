from .modules import FastAPI, subprocess, PUBLIC_DIR, STATIC_DIR, AuthJWTException, JSONResponse
from api_studia.routes.api.kelas import kelas_route
from api_studia.routes.api.tugas import tugas_route
from api_studia.routes.api.users import user_route

app = FastAPI(
    title="API Studia",
    description="API and web interface administration for Studia",
    version="0.1.0",
    extra={"author": "Kelompok 7"},
    debug=True,
)


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )


app.include_router(kelas_route)
app.include_router(tugas_route)
app.include_router(user_route)


def start():
    cmd = ["poetry", "run", "uvicorn", "api_studia.app:app", "--reload", "--host", "127.0.0.1", "--port", "8000"]
    subprocess.run(cmd, shell=True)
