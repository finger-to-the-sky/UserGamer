from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session


from TestProject.database import SessionLocal, engine
from TestProject.test import CreateTestUsers
from TestProject import models, schemas, crud

models.Base.metadata.create_all(bind=engine)


testing = CreateTestUsers()
# testing.create_user("Dead Pe", 33, "213@gmail.com")
# testing.create_game("GTA")
# testing.create_gamer("asdASD", 45, "123123@gmail.com", "RUST")

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/games/", response_model=list[schemas.GameOut])
def get_games(db: Session = Depends(get_db)):
    games = crud.get_games(db)
    return games


@app.get("/user/", response_model=schemas.UserOut)
def get_me(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    return user


@app.post("/connected/")
def connect_to_game(users_id: int, games_id: int, db: Session = Depends(get_db)):
    return crud.connect(db=db, users_id=users_id, games_id=games_id)
