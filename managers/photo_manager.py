
from db import db
from cloud.nextcloud import upload_base64_image
from models.photo_model import TempPhotoModel


class TempPhotoManager:
    def create_photo(photo_data):
        base64_photo = photo_data.pop("photo_base64")
        photo_url = upload_base64_image(base64_photo)
        photo_data["photo_url"] = photo_url
        photo = TempPhotoModel(**photo_data)
        db.session.add(photo)
        db.session.commit()
        return photo