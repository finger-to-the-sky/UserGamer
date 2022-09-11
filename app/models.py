from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


gaming_users = Table("gaming_users", Base.metadata,
                     Column("games_id", ForeignKey("games.id"), primary_key=True),
                     Column("users_id", ForeignKey("users.id"), primary_key=True))


class Games(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    users = relationship("Users",
                         secondary=gaming_users,
                         back_populates="games")


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    games = relationship("Games",
                         secondary=gaming_users,
                         back_populates="users")
