import speech_recognition as sr
import os
import subprocess

recog = sr.Recognizer()
a = ""
cmd2 = ""
ext={"text": [".txt"],
    "word": [".doc", ".docx"],
    "pdf": [".pdf"],
    "image": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "audio": [".mp3", ".wav", ".flac", ".aac"],
    "video": [".mp4", ".avi", ".mkv", ".mov"],
    "spreadsheet": [".xls", ".xlsx", ".csv"],
    "presentation": [".ppt", ".pptx"],
    "code": [".py", ".java", ".cpp", ".html", ".css"],
    "archive": [".zip", ".tar", ".rar"],
    "executable": [".exe", ".app"],
    "database": [".db", ".sqlite", ".dbf"]}

def recognize():
    with sr.Microphone() as source:
        print("Say Command!")
        audio = recog.listen(source, timeout=3, phrase_time_limit=10)
    try:
        a = recog.recognize_google(audio)
        print("You said:", a)
    except sr.UnknownValueError:
        print("Couldn't hear that!")

    return a

def start(app, appname, apptype):
    if apptype == "preinstalled" or apptype == "pre installed":
        subprocess.run(["start", f"ms-{appname}:"], shell=True)
        print("Starting application...")
    elif apptype == "installed":
        os.system(f"start {appname}")
        print("Starting application...")
    else:
        print("Please specify app type as 'preinstalled' or 'installed' as 3rd argument.")

def open(file, fname, ftype):
    for x in range(len(ext[ftype])):
        try:
            os.startfile(fname+ext[ftype][x])
        except FileNotFoundError:
            continue
        except ValueError:
            print("Please specify file type as 3rd argument.")
        else:
            print("Opening file...")
            break
b = recognize()
cmd1 = b[0:b.index(" ")]
cmd2 = b[b.index(" ") + 1:len(b)]
if cmd1 == "start":
    appname = cmd2[0:cmd2.index(" ")]
    apptype = cmd2[cmd2.index(" ") + 1:len(cmd2)]
    start(cmd2, appname, apptype)

if cmd1 == "open":
    fname = cmd2[0:cmd2.index(" ")]
    ftype = cmd2[cmd2.index(" ") + 1:len(cmd2)].lower()
    open(cmd2, fname, ftype)
