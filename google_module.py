import re
import webbrowser

if 'open google' in command:
    reg_ex = re.search('open google (.*)', command)
    url = "https://www.google.com/"
    if reg_ex:
        subgoogle = reg_ex.group(1)
        url = url + 'r/' + subreddit

    webbrowser.open(url)
    print("Done")
