# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class ScrapernbsPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.con = sqlite3.connect("NBS_scrapes.db")
        self.cur = self.con.cursor()

    def create_table(self):
        self.cur.execute("""DROP TABLE IF EXISTS articles_info""")
        self.cur.execute("""CREATE TABLE articles_info(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            date TEXT,
            tags TEXT,
            text TEXT NOT NULL,
            links TEXT
            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        global ident
        
        #url is the primary key, this won't allow
        #for duplicates to exist in the database.
        
        self.cur.execute("""INSERT INTO articles_info VALUES (NULL,?,?,?,?,?,?)""",(
            str(item["url"]),
            str(item["title"]),
            str(item["date"]),
            str(item["labels"]),
            str(item["text"]),
            str(item["links"])
            ))
        self.con.commit()
