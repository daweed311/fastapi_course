from typing import Optional
from sqlalchemy import String, Integer
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Define the async engine and session maker
engine = create_async_engine("sqlite+aiosqlite:///tasks.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)

# Base class for models
class Model(DeclarativeBase):
    pass

# Task ORM model
class TaskOrm(Model):
    __tablename__ = "tasks"

    # Defining columns with explicit types and attributes
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)  # Non-nullable column
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)  # Nullable column for Optional type

# Function to create tables
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

# Function to delete tables
async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
