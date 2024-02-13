from ninja import Router

from authentication.auth_classes import BearerUniqueIdAuth
from orders.commands import CreateEmployeeCommand
from orders.models import Order
from orders.schemas import OrderInSchema, OrderListSchema

router = Router(tags=["orders"])


@router.post("/", response=None, auth=BearerUniqueIdAuth())
def create_order(request, payload: OrderInSchema):
    CreateEmployeeCommand(create_schema=payload).execute()
    return None


@router.get("/", response=list[OrderListSchema], auth=BearerUniqueIdAuth())
def order_list(request):
    orders = Order.objects.filter(category_id=request.user.liked_category_id)
    return [OrderListSchema.parse_obj(order) for order in orders]
