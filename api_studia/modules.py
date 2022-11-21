from fastapi import FastAPI, Depends, Request, Response, status, HTTPException, APIRouter
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.background import BackgroundTasks
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os
import pathlib
import subprocess


PUBLIC_DIR = os.path.join(pathlib.Path().absolute().parent, "public")

STATIC_DIR = os.path.join(pathlib.Path().absolute().parent, "public/asset")

DB_URI = "postgresql://postgres:root@localhost/studia"

template = Jinja2Templates(directory=PUBLIC_DIR)
