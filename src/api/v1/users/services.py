from api.v1.users.schemas import (
    RequestFavorSchema
)
import firebase
from core.settings import settings
from core.utils.responses import create_envelope_response

class FirebaseFavorService:


    def _int_(self):
        self.firebase_session = firebase.FirebaseApplication(settings.FIREBASE_URL, None)

    def convertToDict(self, model: RequestFavorSchema):

        return {
            'user_name': model.user_name,
            'client': model.client,
            'latitude': model.latitude,
            'longitude': model.longitude,

        }

    def create(self, model: RequestFavorSchema):
        self.firebase_session.post("/favors", self.convertToDict(model))
        return create_envelope_response(data=None,message=None,success=True)

