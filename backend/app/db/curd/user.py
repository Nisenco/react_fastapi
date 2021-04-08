from typing import Optional, Dict
from sqlalchemy.orm import Session
from app.db.models import User
from app.utils.security import make_password


def get_user_by_account(db_session: Session, account: str) -> Optional[User]:
    return db_session.query(User).filter(User.account == account).first()


def change_password_by_account(db_session: Session, password: str, user: User) -> User:
    new_password = make_password(password)
    user.hashed_password = new_password
    # db_user = User(**user, hashed_password=new_password)
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user
