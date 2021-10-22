from RPA.Browser.Selenium import Selenium
import time


sel = Selenium()


def test_workforce():
    sel.open_available_browser("https://yoobot.com.br/")
    sel.maximize_browser_window()
    time.sleep(5)


if __name__ == "__main__":
    test_workforce()
