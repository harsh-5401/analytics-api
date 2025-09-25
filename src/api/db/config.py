from decouple import config as decouple_config
import os


# Check if we're running inside Docker
if os.path.exists('/.dockerenv'):
    # Inside Docker container - use docker service name
    DATABASE_URL = decouple_config("DATABASE_URL_DOCKER", 
                                 default="postgresql+psycopg://time-user:time-pw@db_service:5432/timescaledb")
else:
    # Outside Docker (local development) - use localhost
    DATABASE_URL = decouple_config("DATABASE_URL_LOCAL", 
                                 default="postgresql+psycopg://time-user:time-pw@localhost:5432/timescaledb")

DB_TIMEZONE=decouple_config("DB_TIMEZONE" , default="UTC")