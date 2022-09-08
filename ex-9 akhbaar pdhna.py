# AKHBAAR PDHKR SUNAO
# from win32com.client import Dispatch
#
# speak=Dispatch("SAPI.Spvoice")
# speak.Speak("Nehal motherfucker chutiye?")
#

# use of speak in a fucntion to read a string


import requests
import json

def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)

if __name__=='__main__':
    speak("news for today  get ready for heart breaking news")
    url="https://newsapi.org/v2/everything?q=tesla&from=2021-07-20&sortBy=publishedAt&apiKey=7275fdb9d77e42e68f7334f1aaae9067"
    news=requests.get(url).text
    news_dic=json.loads(news)
    print(news_dic["articles"])
    arts=news_dic["articles"]
    for article in arts:
        print(article["title"])
        speak(article["title"])
        speak("moving on to the next news... be attentive")
    speak("thanks for listening")


