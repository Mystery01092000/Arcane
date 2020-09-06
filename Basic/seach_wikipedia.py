import wikipedia

from Basic.text_to_audio import talk


def wiki_search(content):
    result = wikipedia.search("Pranav Mistry")
    sum = wikipedia.summary(result[0])
    print(sum)
    talk(sum)
