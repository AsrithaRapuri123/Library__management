
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import Annotated
from models import Librarian,Books,Log_Operations
from schemas import  LibrarianDTO,BooksDTO,Log_OperationsDTO,UserDTO,CategoryDTO
from database import get_db

#creating an instance of FastAPI application
app = FastAPI()


# Defining a dependency , Annotated is used to provide metadata about the type of the dependency
#  Depends(get_db) indicates that the dependency is fulfilled by calling the get_db function

db_dependency = Annotated[Session, Depends(get_db)]
