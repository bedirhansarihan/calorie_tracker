import sqlite3
import typing
from utils import *
import string
class Database():

    def __init__(self,db_path):
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        #self.create_food_table()
        #self.extend_database()

    def create_food_table(self):
        # check whether exists or not

        self.c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='food' ''')
        if self.c.fetchone()[0] == 1:
            return

        else:

            self.c.execute(f"""CREATE TABLE food (
                            food_name text,
                            amount integer,
                            carbonhydrate real,
                            protein real,
                            fat real,
                            calories integer
                            )""")

    def add_food_into_table(self, tupled_data):
        insert_data = """INSERT INTO food 
                        (food_name, amount, carbonhydrate, protein, fat, calories) 
                        SELECT ?, ?, ?, ?, ?, ?
                        WHERE NOT EXISTS (
                            SELECT *
                            FROM food
                            WHERE food_name = ?
                        )
                        """
        data_tuple = tupled_data

        self.c.executemany(insert_data, data_tuple)
        self.conn.commit()

    #TODO: add more nutrition

    def extend_database(self):
        alphabet = string.ascii_lowercase

        for letter in alphabet:

            list_data: typing.List[typing.Tuple] = food_search(letter, 25)


            self.add_food_into_table(list_data)

            print('success')

    def get_data(self, food_name):

        self.c.execute(f"SELECT * FROM food where food_name LIKE '%{food_name}%'")
        self.conn.commit()

        rows = self.c.fetchall()
        return rows
