from sys import platform

from Basic.google_search import search_google
from Basic.open_google_chrome import chrome

if __name__ == "__main__":
    print("WELCOME TO COMMAND LINE OF ARCANE BOT")

    print("THERE ARE A LOTS OF DIFFERENT FUNCTIONALITY I CAN PERFORM FOR YOU")
    print("PLEASE GUIDE ME, AND I WILL HELP YOU!")
    platform_os = platform

    #chrome(platform_os) #To open chrome
    search_google("Elon Musk")

