import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://users:pass@localhost/filmInfo")
