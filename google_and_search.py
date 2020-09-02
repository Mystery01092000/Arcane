from selenium import webdriver
from selenium.webdriver.common.keys import Keys


if 'open google and search' in command:
    reg_ex = re.search('open google and search (.*)', command)
    search_for = command.split("search",1)[1]
    url = 'https://www.google.com'
    if reg_ex:
        subgoogle = reg_ex.group(1)
        url = url + 'r/' + subgoogle

    talk("Okay!")
    driver = webdriver.Firefox(executable_path='/path/to/geckodriver')
    driver.get('http://www.google.com')
    search = driver.find_element_by_name('q')
    search.send_keys(str(search_for))
    search.send_keys(Keys.RETURN)

