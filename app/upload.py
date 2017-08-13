import os
import urllib3
import cloudinary
from cloudinary.uploader import upload as cloud_upload


urllib3.disable_warnings()

cloudinary.config(
    cloud_name=os.environ["CLOUDINARY_CLOUD_NAME"],
    api_key=os.environ["CLOUDINARY_API_KEY"],
    api_secret=os.environ["CLOUDINARY_API_SECRET"],
)


def upload_image(filename, tag):
    dic = cloud_upload(filename, tags=tag)
    return dic['url']


if __name__ == "__main__":
    upload_image("screenshot_crop.png", "miyadai-shienka-screen")
