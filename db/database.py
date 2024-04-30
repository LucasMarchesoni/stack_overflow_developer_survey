from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

class DB:
  
  def __init__(self, df):
    self.df = df
  
  def create_db(self):
    engine = create_engine(f'postgresql+psycopg2://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@localhost:5432/{os.environ.get("DB_NAME")}')

    self.df.to_sql('survey', engine, index=False, if_exists='fail')