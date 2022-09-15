"""
TODO: Change Repo path and DVC data path
TRY DVC pull
"""
import os
import pandas as pd
import mysql.connector as mysql
from extract_dataframe import text_to_dataframe, excel_to_dataframe

dvc_news_data_path = 'data/example_data.xlsx'
dvc_jobs_train_data_path = 'data/jobs_desc_training_data.txt'
dvc_jobs_test_data_path ='data/jobs_desc_testing_data.txt'

repository_path = 'https://github.com/KaydeeJR/Prompt_Engineering_Design'

def DBConnect(dbName=None):
    # connect to SQL database
    conn = mysql.connect(host='localhost', user='root', password=os.getenv('mysqlPass'), database=dbName, buffered=True)
    cur = conn.cursor()
    return conn, cur

def createDB(dbName: str) -> None:
    conn, cur = DBConnect()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()

def createTable(dbName, sqlFilePath) -> None:
    conn, cur = DBConnect(dbName)
    sqlFile = sqlFilePath
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            cur.execute(command)
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()
    return

def insert_to_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    conn, cur = DBConnect(dbName)
    for _, row in df.iterrows():
        if table_name.__eq__("newsarticles"):
            sqlQuery = f"""INSERT INTO {table_name} (Domain, Title, Description, Body, Link, Timestamp, Analyst_Average_Score, Analyst_Rank, Reference_Final_Score)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            data = (row[0], row[1],row[2], row[3], (row[4]), (row[5]), row[6], row[7], row[8])
        else:
            sqlQuery = f"""INSERT INTO {table_name} (Document, Tokens, Relations)
             VALUES(%s, %s, %s);"""
            data = (row[0], str(row[1]),str(row[2]))
        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)


def db_execute_fetch(dBName, tablename, rdf=True, many=False, ) -> pd.DataFrame:
    """
    fetch data from table in database and save as dataframe
    """
    connection, cursor1 = DBConnect(dBName)
    if many:
        cursor1.executemany(operation= 'SELECT * FROM newsarticles;')
    else:
        cursor1.execute(operation='SELECT * FROM newsarticles;')

    # get column names
    field_names = [i[0] for i in cursor1.description]

    # get column values
    res = cursor1.fetchall()

    # get row count and show info
    nrow = cursor1.rowcount
    if tablename:
        print(f"{nrow} records fetched from {tablename} table")

    cursor1.close()
    connection.close()

    # return result
    if rdf:
        return pd.DataFrame(res, columns=field_names)
    else:
        return res

if __name__ == "__main__":
       # creating database
    createDB(dbName='prompt_engineering')
    # creating tables for each dataset
    createTable(dbName='prompt_engineering',sqlFilePath= os.getcwd()+'\\scripts\\news_db_schema.sql')
    createTable(dbName='prompt_engineering',sqlFilePath= os.getcwd()+'\\scripts\\jobs_db_schema.sql')
    # read data from excel file
    example_dataframe = excel_to_dataframe(filePath=dvc_news_data_path, repository= repository_path, version='v1.0') # shape -> (10, 8)
    # read data from text files
    train_dataframe = text_to_dataframe(filePath=dvc_jobs_train_data_path, repository= repository_path) # shape -> (22, 3) 
    test_dataframe = text_to_dataframe(filePath=dvc_jobs_test_data_path, repository= repository_path) # shape -> (11, 3)
    # add data to the database tables
    insert_to_table(dbName='prompt_engineering', df=example_dataframe, table_name='newsarticles')
    insert_to_table(dbName='prompt_engineering', df=train_dataframe, table_name='jobsdesc')
    insert_to_table(dbName='prompt_engineering', df=test_dataframe, table_name='jobsdesc')