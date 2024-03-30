
from db import db
from cloud.nextcloud import upload_base64_image
from models.photo_model import TempPhotoModel, HomePhotoModel
from utils.geo import image_coordinates


class TempPhotoManager:
    @staticmethod
    def create_photo(photo_data):
        base64_photo = photo_data.pop("photo_base64")
        photo_url = upload_base64_image(base64_photo)
        
        photo_data["photo_url"] = photo_url
        photo = TempPhotoModel(**photo_data)
        db.session.add(photo)
        db.session.commit()
        try:
            coordinates = image_coordinates(base64_photo)
            photo.latitude = str(coordinates["geolocation_lat"])
            photo.longitude = str(coordinates["geolocation_lng"])
        except:
            print("error happened in image coordinates")
        return photo
    
    @staticmethod
    def move_temp_photo(photo_id, home_id):
        temp_photo = TempPhotoModel.query.filter_by(id=photo_id).first()
        HomePhotoManager.create_photo_from_temp(temp_photo, home_id)
        return temp_photo.photo_url


class HomePhotoManager:
    @staticmethod
    def create_photo_from_temp(temp_photo: TempPhotoModel, home_id):
        home_photo = HomePhotoModel()
        home_photo.photo_url = temp_photo.photo_url
        home_photo.home_id = home_id
        db.session.add(home_photo)
        db.session.commit()

    @staticmethod
    def select_home_photo(home_id):
        photo = HomePhotoModel.query.filter_by(home_id=home_id).first()
        if photo:
            photo_url = photo.photo_url
        else:
            photo_url = None
        return photo_url
    