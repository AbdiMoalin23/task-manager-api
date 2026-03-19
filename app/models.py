from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship #Tools to define tables
from typing import List
from datetime import datetime
from sqlalchemy import Integer,String, Boolean, DateTime, ForeignKey #defines database column types
from database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    hashed_password: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    tasks: Mapped[List["Task"]] = relationship(back_populates="owner")

class Task(Base): 
    __tablename__ = "tasks"
    title: Mapped[str] = mapped_column(String)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    owner: Mapped["User"] = relationship(back_populates="tasks")