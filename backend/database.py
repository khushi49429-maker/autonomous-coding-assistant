import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("localhost"),
    port=int(os.getenv("3306")),
    user=os.getenv("root"),
    password=os.getenv("khushigupta@123"),
    database=os.getenv("ai_assistant")
)

cursor = conn.cursor()
print("Database connected successfully!")