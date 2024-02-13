from ninja import Router

from authentication.commands import RegisterUserCommand
from authentication.schemas import RegisterOutSchema, RegisterSchema

router = Router(tags=["authentication"])


@router.post("/register/", response=RegisterOutSchema)
def register(request, payload: RegisterSchema):
    unique_id = RegisterUserCommand(register_schema=payload).execute()
    return {"unique_id": unique_id}
