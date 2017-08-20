import os
import urllib3
import cloudinary
from cloudinary.uploader import upload


def init_upload():
    urllib3.disable_warnings()

    cloudinary.config(
        cloud_name=os.environ["CLOUDINARY_CLOUD_NAME"],
        api_key=os.environ["CLOUDINARY_API_KEY"],
        api_secret=os.environ["CLOUDINARY_API_SECRET"],
    )


def upload_image(filename, tag):
    dic = upload(filename, tags=tag)
    return dic['secure_url']


init_upload()
