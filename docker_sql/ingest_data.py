
from sqlalchemy import create_engine
import pandas as pd
from time import time
import argparse

def main(params):
  user = params.user
  password = params.password
  host = params.host
  port = params.port
  db = params.db
  table_name = params.table_name
  csv_name = 'data.csv'
  engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

  df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
  df=next(df_iter)


  df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
  df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)

  df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

  df.to_sql(name=table_name, con=engine, if_exists='append')


  while True:
        t_start = time()
        df = next(df_iter)
        
        df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)
        
        df.to_sql(name=table_name, con=engine, if_exists='append')
        
        t_end = time()
        
        print('insert another chunk..., took %.3f second' % ( t_end- t_start))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data into PostgreSQL database.')

    #user, password, host, port, database name, table name
    #url of csv file
    parser.add_argument('--user',help='User name of the database')
    parser.add_argument('--password',help='password of the database')
    parser.add_argument('--host',help='Host name of the database')
    parser.add_argument('--port',help='Port name of the database')
    parser.add_argument('--db',help='database name of the database')
    parser.add_argument('--table_name',help='name of the table in the database')
    # parser.add_argument('url',help='url of the csv file')

    args = parser.parse_args()
    main(args)










