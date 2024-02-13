from dataclasses import dataclass

from orders.models import Order
from orders.schemas import OrderInSchema


@dataclass
class CreateEmployeeCommand:
    create_schema: OrderInSchema

    def execute(self) -> None:
        Order.objects.create(**self.create_schema.dict())
