import pyttsx3
import googletrans as trans
import speech_recognition as sr
from gtts import gTTS

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('volume', 1)
engine.setProperty('rate', 150)
engine.setProperty('voice', voices[1].id)

text = ""
LangRef = {
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Amharic': 'am',
    'Arabic': 'ar',
    'Armenian': 'hy',
    'Bengali': 'bn',
    'Bosnian': 'bs',
    'Catalan': 'ca',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dutch': 'nl',
    'English': 'en',
    'Esperanto': 'eo',
    'Estonian': 'et',
    'Filipino': 'fil',
    'Finnish': 'fi',
    'French': 'fr',
    'Galician': 'gl',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Hebrew': 'iw',
    'Hindi': 'hi',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Indonesian': 'id',
    'Italian': 'it',
    'Japanese': 'ja',
    'Javanese': 'jw',
    'Kannada': 'kn',
    'Khmer': 'km',
    'Korean': 'ko',
    'Lao': 'lo',
    'Latin': 'la',
    'Latvian': 'lv',
    'Lithuanian': 'lt',
    'Macedonian': 'mk',
    'Malay': 'ms',
    'Malayalam': 'ml',
    'Marathi': 'mr',
    'Nepali': 'ne',
    'Norwegian': 'no',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Punjabi': 'pa',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Serbian': 'sr',
    'Sinhalese': 'si',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Somali': 'so',
    'Spanish': 'es',
    'Sundanese': 'su',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Vietnamese': 'vi',
    'Welsh': 'cy',
    'Xhosa': 'xh',
    'Yiddish': 'yi',
    'Yoruba': 'yo',
    'Zulu': 'zu'
}

# Recording voice
recog = sr.Recognizer()
with sr.Microphone() as source:
    print("Say:")
    inaudio = recog.listen(source, timeout=3, phrase_time_limit=10)

# Converting to text
try:
    text = recog.recognize_google(inaudio)
except sr.UnknownValueError:
    print("Could not hear properly. Please restart and say again.")

# Translating
a = input("Enter the language you want to translate from:")
b = input("Enter the language you want to translate to:")
newText = trans(text, LangRef[b], LangRef[a])
print(newText)

tts = gTTS(newText)
tts.save("OutputSpeech.mp3")
file = "OutputSpeech.mp3"
engine.say(newText)
engine.runAndWait()
