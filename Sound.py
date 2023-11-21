from win32com.cliet import Dispatch

speak= Dispatch(("SAPI.SpVoice"))

speak.Speak("Hello")