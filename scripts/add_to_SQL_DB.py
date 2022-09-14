"""
TODO: Change Repo path and DVC data path
"""
import os
import sys
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error
from extract_dataframe import excel_to_dataframe

dvc_data_path = 'data/example_data.xlsx'
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

def createTable(dbName: str) -> None:
    conn, cur = DBConnect(dbName)
    sqlFile = os.getcwd()+'\\scripts\\db_schema.sql'
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            res = cur.execute(command)
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()
    return

def insert_to_news_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    conn, cur = DBConnect(dbName)
    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (Domain, Title, Description, Body, Link, Timestamp, Analyst_Average_Score, Analyst_Rank, Reference_Final_Score)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        data = (row[0], row[1],row[2], row[3], (row[4]), (row[5]), row[6], row[7], row[8])
        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)

def db_execute_fetch(*args, many=False,dBName, tablename, rdf=True) -> pd.DataFrame:
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
    createDB(dbName='news')
    createTable(dbName='news')

    dataframe = excel_to_dataframe(filePath=dvc_data_path, repository= repository_path, version='v1.0')
    insert_to_news_table(dbName='news', df=dataframe, table_name='NewsArticles')
    dataframe = db_execute_fetch(dBName='news', tablename='newsarticles')