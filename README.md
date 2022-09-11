# "UserGamer" - first application on FastAPI
- "UserGamer" - created as part of the test task given to me
- When creating it, I had no experience in API development and working with SQLAlchemy, but I managed to implement the application in the shortest possible time for me.

# Functions
- Creation of user and game models.
- Getting a list of games and users who are connected to them.
- Obtaining information about the user and the games to which he is connected.
- User connection to the game. Creating an object User - Game.
- CreateTestUsers - test class for creating users and games.

# How to launch the application
- After you clone the project in your development environment, you need to install the dependencies from requirements.txt with the | pip install -r requirements.txt
- Then, while in TestProject, to run the application, the command | uvicorn TestProject.api.main:app --reload

