from sqlalchemy.orm import Session

from TestProject.database import engine
from TestProject import models


def get_games(db: Session):
    return db.query(models.Games).all()


def get_user(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()


def connect(users_id: int, games_id: int, db: Session):
    con = models.gaming_users.insert().values(users_id=users_id, games_id=games_id)
    ex = engine.connect()
    ex.execute(con)
    username = [x.name for x in db.query(models.Users.name).filter(models.Users.id == users_id).distinct()]
    gamename = [x.name for x in db.query(models.Games.name).filter(models.Games.id == games_id).distinct()]

    return f'{username[0]} - {gamename[0]}'
