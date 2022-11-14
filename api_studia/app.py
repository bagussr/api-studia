from .modules import FastAPI, subprocess, PUBLIC_DIR, STATIC_DIR

app = FastAPI(
    title="API Studia",
    description="API and web interface administration for Studia",
    version="0.1.0",
    extra={"author": "Kelompok 7"},
    debug=True,
)


@app.get("/")
def root():
    return {"message": "Hello World"}


def start():
    cmd = ["poetry", "run", "uvicorn", "api_studia.app:app", "--reload", "--host", "127.0.0.1", "--port", "8000"]
    subprocess.run(cmd, shell=True)
