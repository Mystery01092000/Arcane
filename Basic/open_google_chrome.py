import webbrowser
import os
import winreg
import shlex

def try_find_chrome_path():
    result = None
    if winreg:
        for subkey in ['ChromeHTML\\shell\\open\\command', 'Applications\\chrome.exe\\shell\\open\\command']:
            try: result = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT, subkey)
            except WindowsError: pass
            if result is not None:
                result_split = shlex.split(result, False, True)
                result = result_split[0] if result_split else None
                if os.path.isfile(result):
                    break
                result = None
    else:
        expected = "google-chrome" + (".exe" if os.name == 'nt' else "")
        for parent in os.environ.get('PATH', '').split(os.pathsep):
            path = os.path.join(parent, expected)
            if os.path.isfile(path):
                result = path
                break
    return result

def chrome(platform_os):

    win_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    mac_path = 'open -a /Applications/Google\ Chrome.app %s'
    url = "http://google.com"

    if platform_os == "win32":
        webbrowser.get(win_path).open(url)
    elif platform_os == "darwin":
        webbrowser.get(mac_path).open(url)
