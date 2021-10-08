import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spvoice")
    speak.speak(str)

if __name__ == '__main__':
    speak("Lets Begin Today's News!")
    url = "https://newsapi.org/v2/everything?q=apple&from=2021-10-03&to=2021-10-03&sortBy=popularity&apiKey=c64a9ae3c5f44ab5ac66dcf5b295b083"
    news = requests.get(url).text
    news_dct = json.loads(news)
    arts = news_dct["articles"]
    for article in arts:
        speak(article["description"])
        speak("Next News !")

