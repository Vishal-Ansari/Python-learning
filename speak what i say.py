# AKHBAAR PDHKR SUNAO
# from win32com.client import Dispatch
#
# speak=Dispatch("SAPI.Spvoice")
# speak.Speak("Nehal motherfucker chutiye?")
#

# use of speak in a fucntion to read a string

def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)

if __name__=='__main__':
    speak("i am here to serve you my lord .. whats the command for me my lord")

