import re

from miyadai_db import MiyadaiDatabaseOutput
from linebot.models.template import CarouselColumn, MessageTemplateAction, URITemplateAction, TemplateSendMessage, \
    CarouselTemplate


class Reply:
    db_out = MiyadaiDatabaseOutput()
    TYPE_TEXT = "text"
    TYPE_CAROUSEL = "carousel"
    MSG_HELP = "ヘルプ"
    MSG_MIYADAI = "宮大"
    MSG_MIYADAI_OLD = "過去宮大"

    @classmethod
    def get_news_list(cls, offset: int=0):
        def shaping_title(title):
            len_title = len(title)
            if len_title > 40:
                send_title = title[:37-len_title] + "..."
            else:
                send_title = title
            return send_title

        record = cls.db_out.fetch_shienka_news_all(offset=offset)
        news_list = []
        for r in range(4):
            dic = record.__next__()
            dic["title"] = shaping_title(dic["title"])
            news_list.append(dic)
        return news_list

    @classmethod
    def create_carousel(cls, offset: int=0):
        news_list = cls.get_news_list(offset=offset)
        carousel_list = [
            CarouselColumn(
                thumbnail_image_url=news_list[r]["url_screen_shot"],
                title=news_list[r]["title"],
                text=news_list[r]["day"],
                actions=[
                    MessageTemplateAction(
                        label="画像を見る",
                        text="宮大" + str(offset + r + 1)
                    ),
                    URITemplateAction(
                        label="URLを開く",
                        uri=news_list[r]["url_news"]
                    )
                ]
            )
            for r in range(4)
        ]

        column_text = str(offset+1) + "〜" + str(offset+4) + "ページです"
        carousel_list.append(
            CarouselColumn(
                thumbnail_image_url="https://www.kuaskmenkyo.necps.jp/miyazaki/UnivImages/宮崎大学画像.jpg",
                title="宮大支援課お知らせBot",
                text=column_text,
                actions=[
                    MessageTemplateAction(
                        label='次のページ',
                        text='過去宮大' + str(offset+4)
                    ),
                    URITemplateAction(
                        label='支援課のサイトはこちら♪',
                        uri='http://gakumu.of.miyazaki-u.ac.jp/gakumu/'
                    )
                ]
            )
        )
        send_carousel = TemplateSendMessage(
            alt_text="宮大お知らせ",
            template=CarouselTemplate(
                columns=carousel_list
            )
        )
        return send_carousel

    @classmethod
    def controller(cls, event_message):
        if cls.MSG_HELP == event_message:
            return cls.msg_help()
        elif cls.MSG_MIYADAI == event_message:
            return cls.msg_miyadai()
        elif cls.MSG_MIYADAI_OLD in event_message:
            return cls.msg_miyadai_old(event_message)
        else:
            return cls.msg_other()

    @classmethod
    def msg_help(cls):
        dic = {"type": cls.TYPE_TEXT,
               "message": "test help",
               "log": "test help"}
        return dic

    @classmethod
    def msg_miyadai(cls):
        dic = {"type": cls.TYPE_CAROUSEL,
               "message": cls.create_carousel(0),
               "log": "test 宮大"}
        return dic

    @classmethod
    def msg_miyadai_old(cls, event_message):
        offset = 0
        # 正規表現
        pattern = r'([+-]?[0-9]+\.?[0-9]*)'
        if re.search(pattern, event_message):
            print_num = int(re.search(pattern, event_message).group(1))
            if 0 < print_num <= 100:
                offset = print_num
            else:
                offset = 0
        dic = {"type": cls.TYPE_CAROUSEL,
               "message": cls.create_carousel(offset),
               "log": "test 過去宮大"}
        return dic

    @classmethod
    def msg_other(cls):
        dic = {"type": cls.TYPE_TEXT,
               "message": "test その他",
               "log": "test その他"}
        return dic
