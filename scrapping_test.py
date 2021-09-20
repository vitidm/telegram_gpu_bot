import os
import psycopg2
import sqlite3 as lite
import requests
from bs4 import BeautifulSoup
from configparser import ConfigParser
from psycopg2 import Error

website_link = "https://www.ldlc.com/es-es/"
link_class = "cat-title"

TOKEN = "2014148400:AAES9zceUvpgB-pfxQ6nr9JY1VQuLrWvwnk"
BOT_ID = "275628413"

# conn = psycopg2.connect(
#     user="postgres",
#     password="47468180K.",
#     host="localhost",
#     port="5432",
#     database="postgres")

def crawling(website_link, link_class):
    # get content of website and parse it
    website_request = requests.get(website_link, timeout=5)
    website_content = BeautifulSoup(website_request.content, 'html.parser')
    
    # extract job description
    jobs_link = website_content.find_all('a', class_ = link_class, href=True)
    
    return jobs_link

def send_message(token, chat_id):
    text_links = crawling(website_link, link_class)
    
    all_links_empty = []
    for text_link in text_links:
        link = str(text_link['href'])

        all_links_empty.append(link)

        send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + link

        response = requests.post(send_text)

    return response.json(), all_links_empty

def connect():
    try:
        # Connect to an existing database
        #DATABASE_URL = os.environ.get('DATABASE_URL')
        #connection = psycopg2.connect(DATABASE_URL)

        conn = psycopg2.connect(
            user="ibvqhpzxrcovsc",
            password="153004037d5e3e3238451ec4ec6c87dc78fda17838a5dcc4695de1d122e9146f",
            host="ec2-3-220-214-162.compute-1.amazonaws.com",
            port="5432",
            database="d9l22mp3132eec")
        connection = conn

        connection.autocommit = True

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

        cursor.execute("CREATE TABLE IF NOT EXISTS jobs (id SERIAL, job TEXT NOT NULL);")
        
        jobs_link_pm, links = send_message(token=TOKEN, chat_id=BOT_ID)
        print(links)

        for item in links:
            job_exists = cursor.execute('SELECT job FROM jobs WHERE job = %s', [item])
        
            if len(cursor.fetchall()) != 1:
                cursor.execute('INSERT INTO jobs (job) VALUES (%s);', [item])
                conn.commit()
            else:
                continue

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
