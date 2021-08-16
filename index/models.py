from django.db import models
from django.db.models.enums import Choices
from django.core.exceptions import ValidationError


from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def non_negative_qty(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s cannot be negative value'),
            params={'value': value},
        )


class GroceryList(models.Model):
    choice = (
        ('Pending', 'pending'),
        ('Bought', 'bought'), 
        ('Not available', 'not available'),
        )
    unit = (
        ('Kgs', 'Kilograms'),
        ('gms', 'grams'), 
        ('pcs', 'pieces'),
        ('ltr', 'litres')
        )

    name = models.CharField(max_length=200)
    quantity = models.FloatField(validators=[non_negative_qty])
    qty_unit = models.CharField(max_length=100, choices=unit)
    status = models.CharField(max_length=100,choices=choice)
    date_created = models.DateField(auto_now_add=False)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.name

