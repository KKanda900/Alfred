# Testing functions for alfred.py
import webbrowser

def searchWeather(text):
    url = "https://www.google.com/search?q=weather+{}".format(text)
    webbrowser.open_new_tab(url)

def main():
    city = "Edison"
    searchWeather(city)

main()