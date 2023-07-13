from werkzeug.exceptions import NotFound

from cloud.nextcloud import upload_base64_image
from models.home_model import HomeModel
from models.user_models import UserModel
from models.visitation_model import VisitationModel
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
    
    @staticmethod
    def select_home_details(home_id):
        home_details = HomeModel.query.filter_by(id=home_id).first()
        home_visitations = VisitationModel.query.filter_by(home_id=home_details.id).all()
        home_details.home_visitations = home_visitations
        return home_details
    
    @staticmethod
    def update_home_by_id(home_data):
        if "photo" in home_data.keys():
            base64_photo = home_data.pop("photo")
            photo_url = upload_base64_image(base64_photo)
            home_data["photo_url"] = photo_url
        home_id = home_data["id"]
        home_q = HomeModel.query.filter_by(id=home_id)
        home = home_q.first()
        if not home:
            raise NotFound("This home does not exist")
        
        home_q.update(home_data)
        db.session.add(home)
        db.session.commit()
        return home
    
    @staticmethod
    def select_all_homes():
        homes = HomeModel.query.all()
        return homes
