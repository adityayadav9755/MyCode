import mysql.connector
import speech_recognition as sr

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Aditya#@2612",
    database = "db1"
)
cursor = db.cursor()
recog = sr.Recognizer()

def run(a):
    cursor.execute(a)
    sql = cursor.fetchall()
    print(sql)
    db.commit()

with sr.Microphone() as source:
    print("Say Command!")
    audio = recog.listen(source, timeout=3)

try:
    a = recog.recognize_google(audio)
    print(a)
    run(a)
except sr.UnknownValueError:
    print("Could not hear properly!")

cursor.close()
db.close()

