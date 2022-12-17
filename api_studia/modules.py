from fastapi import (
    FastAPI,
    Depends,
    Request,
    Response,
    status,
    HTTPException,
    APIRouter,
    UploadFile,
    File,
    Header,
    Form,
    BackgroundTasks,
)
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse, StreamingResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.background import BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException, JWTDecodeError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import List, Optional
from deta import Deta
from PIL import Image
import io
import uvicorn
import os
import pathlib
import subprocess
import dotenv

dotenv.load_dotenv()


PUBLIC_DIR = os.path.join(os.getcwd(), "public")


DB_URI = "postgresql://bagussr:v2_3wmxR_sJKev4f2daEvGkecUHTEwzF@db.bit.io/bagussr/api_studia"

template = Jinja2Templates(directory=PUBLIC_DIR)

deta = Deta("c01kndoq_FqotFbhG1iFiKsJym8Ti6FAKUqUQroZP")
