from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base,relationship
from datetime import datetime
URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/Library_management"
# Creating an Engine  which establishes a connection to the database
engine = create_engine(URL)
Base = declarative_base()

#creating librarian table which inherits from Base class
class Librarian(Base):
    __tablename__ = 'Librarian'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mail = Column(String, nullable=False, unique=True)
    ph_no = Column(Integer, nullable=False)  
    addr = Column(String, nullable=True)
    role= Column(String, nullable=False)
    children = relationship("Log_Operations", back_populates="parent")

#Creating  the Books table which inherits from Base class
class Books(Base): 
    __tablename__ = 'Books'
    ISBN = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)

#Creating the Log_Operations Which inherits from Base class
class Log_Operations(Base):
    __tablename__ = 'Log_Operations'
    log_id=Column(Integer,primary_key=True)
    id= Column(Integer, ForeignKey('Librarian.id'), nullable=False)
    name = Column(String, nullable=False)
    title=Column(String,nullable=False)
    borrow_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=False) 
    time_limit = Column(DateTime, nullable=False)
    parent = relationship("Librarian", back_populates="children")


#Creating all tables
Base.metadata.create_all(engine)
 
#creating a session to perform operations
Session = sessionmaker(bind=engine)
session = Session()