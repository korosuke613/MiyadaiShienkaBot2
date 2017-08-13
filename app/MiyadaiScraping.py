from myModules.Scraping import Scraping
from myModules.ScreenShot import ScreenShot


class MiyadaiScraping(Scraping):
    def __init__(self):
        super().__init__()

    def fetch_shienka_news(self):
        self.set_url("http://gakumu.of.miyazaki-u.ac.jp/gakumu/allnews")
        day = title = url = None
        # class=category-moduleのulタグを指定
        ul = self._soup.findAll("ul", class_="category-module")

        # 月のliタグを指定
        for li_month in ul[0].findAll('li'):
            # 記事のliタグを指定
            for li in li_month.findAll('li'):
                # 日にちのspanタグを指定
                for span in li.findAll('span'):
                    # 文字があればdayに格納
                    if span.string is not None:
                        day = span.string
                # aタグを指定
                for a in li.findAll('a'):
                    # aタグに囲まれているタイトルをtitleに格納
                    title = a.string.strip()
                    # aタグ内のhrefで指定されたURLをurlに格納
                    url = 'http://gakumu.of.miyazaki-u.ac.jp' + a.get('href')

                # 日にち、タイトル、URLの順で辞書_dicに格納
                _dic = {
                    "day": day,
                    "title": title,
                    "url_news": url,
                }

                # ジェネレータとして返す
                yield _dic

    @staticmethod
    def screenshot_news_crop(screen_url):
        # クロップする要素の属性を指定
        element_type = "Id"
        # クロップする要素名を指定
        element_name = "wrapper2"
        # インスタンスを生成するときに保存先ファイル名を指定
        ss = ScreenShot("screenshot.png")
        # screen_urlのスクリーンショットを保存
        ss.screen_shot(screen_url)
        # 保存先ファイル名を変更
        ss.set_file_name("screenshot_crop.png")
        # screen_urlのelement_type属性のelement_nameという要素のスクリーンショットを保存
        ss.screen_shot_crop(screen_url, element_name, element_type)
        # インスタンスの削除
        del ss

    def check_pdf(self, screen_url):
        self.set_url(screen_url)
        div = self._soup.find('div', id='wrapper2')
        as_ = div.findAll('a')
        for a in as_:
            if a.string is not None:
                url = a.get('href')
                if '.pdf' in url:
                    if 'http' in url:
                        pdf_url = url
                    else:
                        pdf_url = 'http://gakumu.of.miyazaki-u.ac.jp' + url
                    return pdf_url
        return None


if __name__ == "__main__":
    sc = MiyadaiScraping()
    dic = sc.fetch_shienka_news()
    print(dic.__next__())
    # for news in dic:
    #    print(news)
