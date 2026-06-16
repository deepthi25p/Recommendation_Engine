from data.database import SessionLocal
from data.repositories import (
    UserRepository,
    ContentRepository
)


def test_database_connection():

    db = SessionLocal()

    assert db is not None

    db.close()


def test_users_exist():

    db = SessionLocal()

    repo = UserRepository(db)

    users = repo.get_all_users()

    assert len(users) > 0

    db.close()


def test_content_exists():

    db = SessionLocal()

    repo = ContentRepository(db)

    content = repo.get_all_content()

    assert len(content) > 0

    db.close()