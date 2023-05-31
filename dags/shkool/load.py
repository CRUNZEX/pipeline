import pandas as pd
# from sqlalchemy import create_engine


# def connectionDB():
# host='postgresLocal',
# database='dataPeople',
# user='local',
# password='password',
# port='5432'

# engine = create_engine('postgresql://local:password@postgresLocal:5432/dataPeople', echo=False) #postgresql://username:password@host:port/database
    # return engine
df = pd.read_csv('/opt/airflow/data/stagingFile.csv')
# df.to_sql('final_data2', con = engine, if_exists='replace',index_label='id')

df.to_csv("/opt/airflow/data/finalFile.csv", index=False) 

