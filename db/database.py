from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

class DB:
  def __init__(self):
    self.engine = create_engine(f'postgresql+psycopg2://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@localhost:5432/{os.environ.get("DB_NAME")}')
  
  def create_db(self, df):
    df.to_sql('survey', self.engine, index=False, if_exists='fail')
    
  def create_connection(self):
    return self.engine
  
  def query_to_dataframe(self, query):
    return pd.read_sql_query(query, self.engine)