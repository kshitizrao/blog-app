from .database import Base
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship



class Blog(Base):
    __tablename__ = "blogs"
    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    title:Mapped[str] = mapped_column(String(100))
    body:Mapped[str] = mapped_column(String(500))
    user_id:Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))

    creator = relationship('User', back_populates='blogs')

class User(Base):
    __tablename__ = "users"
    id:Mapped[int]  = mapped_column(primary_key=True, index=True)   
    username:Mapped[str] = mapped_column(String(50))
    email:Mapped[str] = mapped_column(String(100))
    password:Mapped[str] = mapped_column(String(100))

    blogs = relationship('Blog', back_populates='creator')

