from app.myModules.Scraping import Scraping


class MiyadaiScraping(Scraping):
    def __init__(self):
        super().__init__()

    def shienka_all_news(self):
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
                    "url": url,
                }

                # ジェネレータとして返す
                yield _dic

    def check_pdf(self, screen_url):
        self.set_url(screen_url)
        div = self._soup.find('div', id='wrapper2')
        as_ = div.findAll('a')
        for a in as_:
            if a.string is not None:
                url = a.get('href')
                if '.pdf' in url:
                    pdf_url = 'http://gakumu.of.miyazaki-u.ac.jp' + url
                    return pdf_url
        return None


if __name__ == "__main__":
    sc = MiyadaiScraping()
    dic = sc.shienka_all_news()
    print(dic.__next__())
    # for news in dic:
    #    print(news)
