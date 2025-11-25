import pandas as pd
from sqlalchemy import create_engine

DB_PATH = "sqlite:///prices.db"
engine = create_engine( DB_PATH )

def init_db():
    df = pd.DataFrame( columns = [ "timestamp", "price" ] )
    df.to_sql( "prices", engine, if_exists = "replace", index = False )

def append_price( timestamp, price ):
    df = pd.DataFrame( [ [ timestamp, price ] ], columns = [ "timestamp", "price" ] )
    df.to_sql( "prices", engine, if_exists = "append", index = False)

def load_all():
    return pd.read_sql( "SELECT * FROM prices", engine )
