
from pydantic import BaseModel
from datetime import date,datetime

#creating data transfer object for librarian

class LibrarianDTO(BaseModel):  
    id:int
    name:str
    mail:str
    ph_no:int
    addr:str
    role:str

#creating data transfer object for Books    
class BooksDTO(BaseModel):  
    ISBN:str
    title:str
    author:str

# Data Transfer Object for Book Category inheriting from BooksDTO
class CategoryDTO(BooksDTO):  
    category_id:int
    category_name:str
    shelf_no:int
    quantity:int

#Creating Data Transfer Object for Log Operations
class Log_OperationsDTO(BaseModel):
    log_id:int
    id:int
    name:str
    title:str
    borrow_date:date
    return_date:date
    time_limit:datetime


# Data Transfer Object for User inheriting from LibrarianDTO
class UserDTO(LibrarianDTO):
        status:str
        date_of_reg:datetime


