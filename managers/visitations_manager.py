from models.visitation_model import VisitationModel
from db import db


class VisitationManager:
    @staticmethod
    def select_home_visitations(home_id):
        visitations = VisitationModel.query.filter_by(home_id=home_id).all()
        return visitations

    @staticmethod
    def select_land_visitations(land_id):
        visitations = VisitationModel.query.filter_by(land_id=land_id).all()
        return visitations

    @staticmethod
    def create_visitation(visitation_data):
        visitation = VisitationModel(**visitation_data)
        db.session.add(visitation)
        db.session.commit()
        return visitation
