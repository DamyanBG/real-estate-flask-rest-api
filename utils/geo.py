from exif import Image

import base64
import re
from tempfile import TemporaryDirectory
from uuid import uuid4
from mimetypes import guess_extension


def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == "S" or ref == "W":
        decimal_degrees = -decimal_degrees
    return decimal_degrees


def image_coordinates(base64_image):
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

        with open(temp_file_path, "rb") as src:
            img = Image(src)
        if img.has_exif:
            try:
                img.gps_longitude
                coords = (
                    decimal_coords(img.gps_latitude, img.gps_latitude_ref),
                    decimal_coords(img.gps_longitude, img.gps_longitude_ref),
                )
            except AttributeError:
                print("No Coordinates")
        else:
            print("The Image has no EXIF information")

        return {
            "imageTakenTime": img.datetime_original,
            "geolocation_lat": coords[0],
            "geolocation_lng": coords[1],
        }
