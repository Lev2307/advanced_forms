from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.


class ToppingsModel(models.Model):
    name = models.CharField(max_length=55)

    class Meta:
        verbose_name = 'Toppings'
        verbose_name_plural = 'Toppings'

    def __str__(self):
        return self.name

class PizzaModel(models.Model):
    name = models.CharField(max_length=55)
    name_slug = models.SlugField(blank=True, null=True)
    toppings = models.ManyToManyField(ToppingsModel, verbose_name='toppings')

    class Meta:
        verbose_name = 'My pizza recipes'
        verbose_name_plural = 'Pizza recipes'

    def save(self, *args, **kwargs):
        if not self.name_slug:
            self.name_slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pizza_detail', kwargs={'slug': self.name_slug})

    def all_toppings(self):
        return "\n".join([t.name for t in self.toppings.all()])

    def __str__(self):
        return  f'{self.name}: {", ".join([topping.name for topping in self.toppings.all()])}'

# class ProxyPizza(PizzaModel.toppings.through):
#     class Meta:
#         proxy = True

#     def __str__(self):
#         return str(self.toppingsmodel)