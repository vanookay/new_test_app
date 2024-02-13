from ninja import ModelSchema, Schema

from authentication.models import User


class RegisterSchema(ModelSchema):
    liked_category_id: int

    class Meta:
        model = User
        fields = ["username", "password"]


class RegisterOutSchema(Schema):
    unique_id: str
