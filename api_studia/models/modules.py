from sqlalchemy import Column, Date, Integer, String, create_engine, ForeignKey, Boolean, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from api_studia.service.db_service import Base
import subprocess
import json
import datetime


def upgrade():
    cmd = ["poetry", "run", "alembic", "upgrade", "head"]
    subprocess.run(cmd, shell=True)


def downgrade():
    cmd = ["poetry", "run", "alembic", "downgrade", "base"]
    subprocess.run(cmd, shell=True)


def migrate():
    cmd = ["poetry", "run", "alembic", "revision", "--autogenerate", "-m", "migration"]
    subprocess.run(cmd, shell=True)
