from Basic.open_google_chrome import chrome
import sys

def search_google(content):
    count = 0
    try:
        from googlesearch import search
    except ImportError:
        print("No Module named 'google' Found")
    for i in search(query=content, tld='co.in', lang='en', num=10, stop=1, pause=2):
        count += 1
        print(count)
        print(i + '\n')
        chrome(sys.platform, i)