class Reply:
    TYPE_TEXT = "text"
    TYPE_CAROUSEL = "carousel"
    MSG_HELP = "ヘルプ"
    MSG_MIYADAI = "宮大"
    MSG_MIYADAI_OLD = "過去宮大"

    def __init__(self):
        pass

    @classmethod
    def controller(cls, event_message):
        if cls.MSG_HELP == event_message:
            dic = {"type": cls.TYPE_TEXT,
                   "message": "test help"}
        elif cls.MSG_MIYADAI == event_message:
            dic = {"type": cls.TYPE_CAROUSEL,
                   "message": "test 宮大"}
        elif cls.MSG_MIYADAI_OLD in event_message:
            dic = {"type": cls.TYPE_CAROUSEL,
                   "message": "test 過去宮大"}
        else:
            dic = {"type": cls.TYPE_TEXT,
                   "message": "test その他"}
        return dic
