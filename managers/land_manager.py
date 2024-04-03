from models.land_model import LandModel
from db import db
from cloud.nextcloud import upload_base64_image


class LandManager:
    @staticmethod
    def create_land(land_data):
        base64_photo = land_data.pop("photo")
        photo_url = upload_base64_image(base64_photo)
        land_data["photo_url"] = photo_url
        land = LandModel(**land_data)
        db.session.add(land)
        db.session.commit()
        return land

    @staticmethod
    def select_all_lands():
        lands = LandModel.query.all()
        return lands

    @staticmethod
    def select_land_by_id(land_id):
        land_q = LandModel.query.filter_by(id=land_id)
        land = land_q.first()
        land.land_views = str(int(land.land_views) + 1)
        db.session.commit()
        return land
