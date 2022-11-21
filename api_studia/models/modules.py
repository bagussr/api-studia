from sqlalchemy import Column, Date, Integer, String, create_engine, ForeignKey, Boolean
from api_studia.service.db_service import Base
import subprocess


def upgrade():
    cmd = ["poetry", "run", "alembic", "upgrade", "head"]
    subprocess.run(cmd, shell=True)


def downgrade():
    cmd = ["poetry", "run", "alembic", "downgrade", "base"]
    subprocess.run(cmd, shell=True)


def migrate():
    cmd = ["poetry", "run", "alembic", "revision",
           "--autogenerate", "-m", "migration"]
    subprocess.run(cmd, shell=True)
