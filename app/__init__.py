import time

from .conf_clicker import FirefoxBrowserZoomClicker
from config import GECKODRIVER_PATH


def run():
    conf_url = input("Ссылка на конфу: ")
    conf_code = input("Код конфы: ")
    nickname = input("Никнейм: ")
    browser_exe_path = input("Введите путь до браузера: ")
    clicker = FirefoxBrowserZoomClicker(
        str(GECKODRIVER_PATH),
        browser_exe_path,
        conf_url,
        conf_code,
        nickname
    )
    clicker.conf_login()
    time.sleep(10)
