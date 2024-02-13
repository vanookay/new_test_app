from django.contrib.auth import get_user_model
from ninja.security import HttpBearer

User = get_user_model()


class BearerUniqueIdAuth(HttpBearer):
    def authenticate(self, request, token):
        user = User.objects.get(unique_id=token)
        request.user = user
        return token
