from ninja import ModelSchema, Schema

from orders.models import Order


class OrderInSchema(ModelSchema):
    category_id: int

    class Meta:
        model = Order
        fields = ['title', 'description']


class OrderListSchema(ModelSchema):
    class Meta:
        model = Order
        fields = ['title', 'description']


class OrderListFilterSchema(Schema):
    category_id: int
