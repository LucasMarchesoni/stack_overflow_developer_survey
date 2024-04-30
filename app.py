from db.database import DB
import pandas as pd

df = pd.read_csv("./data/survey_results_public.csv")
db = DB()

if __name__ == "__main__":
  db.create_db(df)