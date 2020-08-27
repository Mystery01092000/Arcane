import re
import webbrowser

if 'open google' in command:
    reg_ex = re.search('open google (.*)', command)
    url = "https://www.google.com/"
