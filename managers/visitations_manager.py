from models.visitation_model import VisitationModel

class VisitationManager:
    @staticmethod
    def select_home_visitations(home_id):
        visitations = VisitationModel.query.filter_by(home_id=home_id).all()
        return visitations
