
from app.core.database import engine
from app.models.transaction import Base, Transaction


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("NEXORA Finance: database tables created!")


if __name__ == "__main__":
    create_tables()
