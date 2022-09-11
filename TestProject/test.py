from sqlalchemy.orm import Session
from TestProject.database import engine
from TestProject import models


class CreateTestUsers:
    """
        CreateTestUsers - class to create test users, games and players
    """

    def __init__(self):
        self.session = Session(engine)

    def create_user(self, username: str, age: int, email: str):
        """
            create_user() - creates a user without connecting to the game and
            enters it into the database.
        """

        user = models.Users(name=username, age=age, email=email)

        self.session.add(user)
        self.session.commit()
        print('Done!')
        return user

    def create_game(self, game_name: str):
        """
        create_game() - Creates a game with no connected users and
            enters it into the database.
        """

        game = models.Games(name=game_name)

        self.session.add(game)
        self.session.commit()
        print('Done!')
        return game

    def create_gamer(self, username: str, age: int, email: str, game_name: str):
        """
        create_gamer - creates the user "Player" and the game to which this user is connected.
        Then all the data is entered into the database.
        """

        user = models.Users(name=username, age=age, email=email)
        game = models.Games(name=game_name)
        user.games = [game]

        self.session.add_all([user, game])
        self.session.commit()
        print('Done!')
        return user
