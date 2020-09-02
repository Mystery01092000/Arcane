import webbrowser


def chrome(platform_os):

    win_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    mac_path = 'open -a /Applications/Google\ Chrome.app %s'
    url = "http://google.com"

    if platform_os == "win32":
        webbrowser.get(win_path).open(url)
    elif platform_os == "darwin":
        webbrowser.get(mac_path).open(url)
