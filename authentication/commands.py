from dataclasses import dataclass

from authentication.models import User
from authentication.schemas import RegisterSchema
from authentication.utils import generate_unique_id


@dataclass
class RegisterUserCommand:
    register_schema: RegisterSchema

    def execute(self) -> str:
        user = User.objects.create(
            **self.register_schema.dict(),
            unique_id=generate_unique_id(),
        )
        return user.unique_id
