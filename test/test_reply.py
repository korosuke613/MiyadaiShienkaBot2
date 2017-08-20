from app.reply import Reply


def test_reply_controller_1():
    msg = Reply.MSG_MIYADAI
    value = Reply.controller(msg)

    assert value["type"] == Reply.TYPE_CAROUSEL


def test_reply_controller_2():
    msg = Reply.MSG_MIYADAI_OLD
    value = Reply.controller(msg)

    assert value["type"] == Reply.TYPE_CAROUSEL


def test_reply_controller_3():
    msg = Reply.MSG_MIYADAI_OLD + "1"
    value = Reply.controller(msg)

    assert value["type"] == Reply.TYPE_CAROUSEL


def test_reply_controller_4():
    msg = Reply.MSG_HELP
    value = Reply.controller(msg)

    assert value["type"] == Reply.TYPE_TEXT


def test_reply_controller_5():
    msg = "あああああ"
    value = Reply.controller(msg)

    assert value["type"] == Reply.TYPE_TEXT
