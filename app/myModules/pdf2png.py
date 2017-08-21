from os.path import isfile, splitext
from subprocess import check_call, CalledProcessError

import requests


def convert(pdf):
    """Convert a PDF to JPG"""
    if not isfile(pdf):
        print("ERROR", "Can't find {0}".format(pdf))
        return

    png = splitext(pdf)[0] + ".png"
    pdf = pdf + "[0]"

    try:
        check_call(["convert", "-background", "white", "-flatten", "-density", "144", pdf, png])
        print("Converted", "{0} converted".format(pdf))
    except (OSError, CalledProcessError) as e:
        print("ERROR", "ERROR: {0}".format(e))


def download_pdf(pdf_url, file_name):
    r = requests.get(pdf_url)
    # ファイルの保存
    # TODO withにする
    if r.status_code == 200:
        f = open(file_name, 'wb')
        f.write(r.content)
        f.close()
