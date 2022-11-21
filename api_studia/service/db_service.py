from api_studia.modules import create_engine, sessionmaker, DB_URI, declarative_base
from api_studia.sql_app import models

engine = create_engine(DB_URI, echo=True)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()
