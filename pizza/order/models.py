from django.db import models
from pizzas.models import PizzaModel

# Create your models here.
class OrderModel(models.Model):
    address = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    pizza_order = models.ManyToManyField(PizzaModel)

    class Meta:
        verbose_name = "Orders"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f'Some Address: {self.address}, Order: {", ".join([j.name for j in self.pizza_order.all()])}'

    def all_orders(self):
        return "\n".join([o.name for o in self.pizza_order.all()])

class OrderProxy(OrderModel.pizza_order.through):
    class Meta:
        proxy = True

    def __str__(self):
        return str(self.ordermodel)