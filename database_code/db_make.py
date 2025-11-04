"""
I need to import the models before i will call the
create_db fun i need to remember this always
"""

from pathlib import Path


from sqlmodel import SQLModel, create_engine


from config_settings import DATABASE_FILE_NAME

from database_code.models_table import CategoryModel, ProductModel  # type: ignore

# I need to import this so that i am calling the models before calling the making of the database


sqlite_file_path = Path.cwd() / DATABASE_FILE_NAME


sqlite_url = f"sqlite:///{sqlite_file_path}"


engine = create_engine(url=sqlite_url)


def create_db_and_engine():
    """
    This will create the database file / connection and i need to call this
    in the main.py file so that database will be established easily
    """

    sqlite_file_path.parent.mkdir(exist_ok=True)
    SQLModel.metadata.create_all(engine)
