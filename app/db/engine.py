import os
from pathlib import Path
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

def load_root_env():
    current_dir = Path(__file__).parent
    env_path = current_dir / '.env'

    while not env_path.exists() and current_dir != current_dir.parent:
        current_dir = current_dir.parent
        env_path = current_dir / '.env'

    if env_path.exists():
        load_dotenv(env_path)
        return True

    return False

load_root_env()
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASSWORD')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

DATABASE_URL = f'postgresql://{db_user}:{db_pass}@db:{db_port}/{db_name}'
Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=False)

Session = sessionmaker(bind=engine)
    

