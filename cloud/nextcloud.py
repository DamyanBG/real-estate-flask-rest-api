import base64
import re
import nextcloud_client
from tempfile import TemporaryDirectory
from uuid import uuid4
from mimetypes import guess_extension
from decouple import config

NEXTCLOUD_USER = config("NEXTCLOUD_USER")
NEXTCLOUD_PASS = config("NEXTCLOUD_PASSWORD")


def upload_base64_image(base64_image):
    extension_container, base64_data = base64_image.split(",")
    photo_bytes = base64.b64decode(base64_data.encode("utf-8"))
    match = re.search(":(.+);", extension_container)
    mime_type = match.group(1)
    file_extension = guess_extension(mime_type)
    file_name = f"{uuid4()}{file_extension}"

    with TemporaryDirectory() as temp_dir:
        temp_file_path = f"{temp_dir}/{file_name}"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(photo_bytes)

        nc = nextcloud_client.Client("https://dymboto.chickenkiller.com")
        nc.login(NEXTCLOUD_USER, NEXTCLOUD_PASS)
        nc.put_file(f"real-estate-dev/{file_name}", temp_file_path)
        link_info = nc.share_file_with_link(f"real-estate-dev/{file_name}")
        link = link_info.get_link()

        print("Here is your link: " + link)

        preview_link = f"{link}/preview"
        return preview_link
