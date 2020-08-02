import matplotlib.pyplot as plt
import pandas as pd
import os
import psycopg2



class Data:
    def __init__(self):
        self.login = os.environ['envname']
        self.passcode = os.environ['envpass']
        self.dbname = "postgres"

    def show_performance(self):
        word_data = pd.read_csv('words/word_data.csv')
        df = pd.DataFrame(data=word_data)
        df.plot(x="Word", color=['b', 'r'], kind='barh')
        plt.xlabel("Trials")
        plt.show()

    def senddata(self):
        conn = psycopg2.connect(host="localhost", database="postgres",
                                user=self.login, password=self.passcode)
        sql = """CREATE TABLE player_name(
              id SERIAL PRIMARY KEY,
              word CHAR(20),
              positive INT,
              negative INT)
              """
        try:
            cur = conn.cursor()
            cur.execute('DROP TABLE IF EXISTS player_name')
            cur.execute(sql)
            conn.commit()
            cur.close()
            print('Table created!')
        except psycopg2.DatabaseError as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

    def adddata(self):
        conn = psycopg2.connect(host="localhost", database="postgres",
                                user=self.login, password=self.passcode)
        sql = """INSERT INTO player_name(word, positive, negative)"""
        word_data = pd.read_csv('words/word_data.csv')
        df = pd.DataFrame(data=word_data)
        try:
            cur = conn.cursor()
            for row in df.itertuples():
                cur.execute("""
                INSERT INTO player_name(word, positive, negative)
                VALUES (%s, %s, %s)""",
                (row.Word, row.Positive, row.Negative))
            conn.commit()
            cur.close()
        except psycopg2.DatabaseError as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Done')


    def sendsql(self):
        conn = psycopg2.connect(host="localhost", database=self.dbname,
                                user=self.login, password=self.passcode)
        try:
            cur = conn.cursor()
            cur.execute('SELECT version()')
            db_version = cur.fetchone()
            print(db_version)
            cur.close()
        except psycopg2.DatabaseError as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")



data = Data()
data.adddata()
