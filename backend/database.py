
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://beatsense_user:LZbrzZ6gIF3STaCebz6niLvGvc5QCA4k@dpg-d9g45l4m0tmc73b7o5dg-a.oregon-postgres.render.com/beatsense"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)