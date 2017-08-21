"""
Documentation for this module.

More details.
"""

from PIL import Image
from selenium import webdriver


class ScreenShot:
    def __init__(self, file_name_: str = "screenshot.png"):
        """コンストラクタ
        @type file_name_: str
        """
        self._filename = file_name_
        self._driver = webdriver.PhantomJS()
        self._driver.set_window_size(1024, 768)
        self._crop_margin = 0

    def screen_shot(self, url_: str) -> bool:
        """urlで指定したページのスクリーンショットを撮る関数
        @return Success is True, Fail is False
        @param url_: the webpage to save screenshot
        """
        try:
            self._driver.get(url_)
            self._driver.save_screenshot(self._filename)
        except Exception as e:
            print(e)
            return False
        return True

    def screen_shot_crop(self, url_: str, search_element_name: str, search_element_type: str = "Id") -> bool:
        """urlで指定したページのスクリーンショットを撮り、要素名と要素の型でクロップする関数
        @return 成功したかどうかをboolで返す
        @param url_: スクリーンショットを撮るURL
        @param search_element_name: 検索する要素名
        @param search_element_type: 検索する要素の型
        """
        self.screen_shot(url_)
        before_script = """
                        var element = document.getElementBy""" + search_element_type + "('" + search_element_name + """');
                        var rect = element.getBoundingClientRect(); 
                        """
        try:
            left = self._driver.execute_script(before_script + "return rect.left;") - self._crop_margin
            top = self._driver.execute_script(before_script + "return rect.top;")
            right = self._driver.execute_script(before_script + "return rect.width;") + left + self._crop_margin
            bottom = self._driver.execute_script(before_script + "return rect.height;") + top + self._crop_margin
        except Exception as e:
            print(e)
            return False
        im = Image.open(self._filename)
        im = im.crop((left, top, right, bottom))
        im.save(self._filename)
        im.close()
        return True

    def set_file_name(self, filename_: str):
        """保存ファイル名を設定する
        @param filename_: ファイル名
        """
        self._filename = filename_

    def set_window_size(self, width_: int, height_: int):
        """PhantomJSのウィンドウサイズを設定する
        @param width_: 横幅(pixel)
        @param height_: 縦幅(pixel)
        """
        self._driver.set_window_size(width=width_, height=height_)

    def get_window_size(self) -> object:
        """PhantomJSのウィンドウサイズを取得する
        @return ウィンドウサイズのリスト
        """
        return self._driver.get_window_size()

    def set_crop_margin(self, crop_margin_: int):
        """クロップ時のマージンを設定する
        @param crop_margin_: マージン(pixel)
        """
        self._crop_margin = crop_margin_

    def get_crop_margin(self) -> object:
        """クロップ時のマージンを取得する
        @return: マージン(pixel)
        """
        return self._crop_margin

    def __del__(self):
        """デストラクタ"""
        self._driver.close()
