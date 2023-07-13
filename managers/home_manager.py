from cloud.nextcloud import upload_base64_image
from models.home_model import HomeModel
from db import db

class HomeManager:
    @staticmethod
    def add_home(home_data):
        base64_photo = home_data.pop("photo")
        photo_url = upload_base64_image(base64_photo)
        home_data["photo_url"] = photo_url
        home = HomeModel(**home_data)
        db.session.add(home)
        db.session.commit()
        return home
    
    @staticmethod
    def select_home_by_id(home_id):
        home = HomeModel.query.filter_by(id=home_id).first()
        return home
