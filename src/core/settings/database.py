from collections.abc import Generator
import sentry_sdk
from models.base_model import Base as BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy import select

from core.settings import log, settings
from core.utils.exceptions import BaseAppException

engine = create_engine(
    settings.POSTGRESQL_URL.unicode_string(),
    poolclass=NullPool,
    connect_args={"application_name": "fee-api-service"},
)
Session = sessionmaker(bind=engine, autocommit=False)


def get_session() -> Generator:
    log.info("Getting db session")
    db = Session()
    log.info("DB session has been stablished")
    try:
        yield db
    except Exception as exc:  # noqa: BLE001
        db.rollback()
        sentry_sdk.capture_exception(exc)
        log.info(exc)
    finally:
        db.close()


def create_schemas():
    schema_format = "CREATE SCHEMA IF NOT EXISTS {}"
    query_schema_public = text(schema_format.format("public"))

    with engine.connect() as conn:
        with conn.begin():
            conn.execute(query_schema_public)
            
        conn.close()

def validate_db_conections():
    try:
        session = next(get_session())
        log.info("Connection 💲 Success")

    except Exception as e:
        session.close()
        message_error = f"Error on validate_db_conections, message error: {e}"
        raise BaseAppException(message_error)
  
def init_db():
    create_schemas()
    BaseModel.metadata.create_all(engine)