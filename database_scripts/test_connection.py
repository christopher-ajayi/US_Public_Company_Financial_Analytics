from database_db_core.connection import get_db_engine

engine = get_db_engine()

try:
    with engine.connect() as conn:
        print("PostgreSQL connection successful")

except Exception as e:
    print("Connection failed")
    print(e)