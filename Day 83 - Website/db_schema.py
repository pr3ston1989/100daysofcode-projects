from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, LargeBinary, DateTime, Boolean, PrimaryKeyConstraint
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
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    post_author = relationship("User", back_populates="user_posts")
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
    post_comments = relationship("PostComment", back_populates="parent_post")
    post_tags = relationship("PostTags", back_populates="parent_post")
    post_category = relationship("PostCategory", back_populates="parent_post")


class PostComment(db.Model):
    __tablename__ = "post_comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("posts.id"))
    parent_post = relationship("BlogPost", back_populates="post_comments")
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="user_comments")
    parent_id: Mapped[int] = mapped_column(Integer)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[str] = mapped_column(DateTime, nullable=False)
    edited_at: Mapped[str] = mapped_column(DateTime)
    published_at: Mapped[str] = mapped_column(DateTime)
    content: Mapped[str] = mapped_column(String, nullable=False)

class Category(db.Model):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    parent_id: Mapped[int] = mapped_column(Integer)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    meta_title: Mapped[str] = mapped_column(String(100), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)


class PostCategory(db.Model):
    __tablename__ = "post_category"
    category_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("categories.id"))
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("posts.id"))
    __table_args__ = (PrimaryKeyConstraint("category_id", "post_id", name="id"),)
    parent_post = relationship("BlogPost", back_populates="post_category")

class Tag(db.Model):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    meta_title: Mapped[str] = mapped_column(String(100), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)


class PostTags(db.Model):
    __tablename__ = "post_tags"
    tag_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("tags.id"))
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("posts.id"))
    __table_args__ = (PrimaryKeyConstraint("tag_id", "post_id", name="id"),)
    parent_post = relationship("BlogPost", back_populates="post_tags")
