import os.path
import pytest

from app.myModules.pdf2png import download_pdf, convert

url = "http://gakumu.of.miyazaki-u.ac.jp/gakumu/images/campuslife/scholarship/H29/ooame20170705.pdf"
not_url = "http://gakumu.of.miyazaki-u.ac.jp/gakumu/images/campuslife/scholarship/H29/"


@pytest.fixture()
def fixture_rm_pdf():
    if os.path.isfile("test.pdf") is True:
        os.remove("test.pdf")
    if os.path.isfile("test.png") is True:
        os.remove("test.png")
    yield True
    if os.path.isfile("test.pdf") is True:
        os.remove("test.pdf")
    if os.path.isfile("test.png") is True:
        os.remove("test.png")


def test_download_pdf1(fixture_rm_pdf):
    download_pdf(url, "test.pdf")

    assert os.path.isfile("test.pdf")


def test_convert1(fixture_rm_pdf):
    download_pdf(url, "test.pdf")
    convert("test.pdf")
    assert os.path.isfile("test.png")


def test_download_pdf2(fixture_rm_pdf):
    download_pdf(not_url, "test.pdf")
    assert os.path.isfile("test.pdf") is False
