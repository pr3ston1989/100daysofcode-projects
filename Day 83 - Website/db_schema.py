from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, LargeBinary, DateTime, Boolean
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    login: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(50))
    middle_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(100), nullable=False)
    registered_at: Mapped[str] = mapped_column(DateTime, nullable=False)
    last_login: Mapped[str] = mapped_column(DateTime, nullable=False)
    intro: Mapped[str] = mapped_column(String)
    profile: Mapped[str] = mapped_column(String)
    avatar: Mapped[bytes] = mapped_column(LargeBinary)
    user_posts = relationship("BlogPost", back_populates="post_author")
    user_comments = relationship("Comment", back_populates="comment_author")

class BlogPost(db.Model):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.is"))
    author = relationship("User", back_populates="user_posts")
    parent_id: Mapped[int] = mapped_column(Integer)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    meta_title: Mapped[str] = mapped_column(String(100), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), nullable=False)
    summary: Mapped[str] = mapped_column(String)
    published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[str] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[str] = mapped_column(DateTime)
    published_at: Mapped[str] = mapped_column(DateTime)
    content: Mapped[str] = mapped_column(String, nullable=False)
    post_image: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    #TODO: uzupełnić po utworzeniu pozostałych tabel
    post_comments = relationship()
    post_tags = relationship()
    post_category = relationship()

