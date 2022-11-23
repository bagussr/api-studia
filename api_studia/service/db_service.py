from api_studia.modules import create_engine, sessionmaker, DB_URI, declarative_base

engine = create_engine(DB_URI)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()
