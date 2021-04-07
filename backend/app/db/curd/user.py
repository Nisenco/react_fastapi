from typing import Optional
from sqlalchemy.orm import Session
from app.db.models import User


def get_user_by_account(db_session: Session, account: str) -> Optional[User]:
    return db_session.query(User).filter(User.account == account).first()
