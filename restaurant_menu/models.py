from django.db import models
from django.contrib.auth.models import User


MEAL_TYPE = (
    # ("used in the code"," displayed in the frontend")
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts"),
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available"),
)


class MenuItem(models.Model):
    # unique=True to ensure no duplicates
    meal = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    meal_type = models.CharField(choices=MEAL_TYPE, max_length=200)

    # Many to one relationship ,
    # CASCADE deletes the menu item if the user is deleted
    # PROTECT prevents the deletion
    # SET_NULL sets the author to null but does not delete
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    status = models.IntegerField(choices=STATUS, default=1)

    # auto_now_add - the date is set when the object is created
    date_created = models.DateTimeField(auto_now_add=True)

    # auto_now - the date is set when the object is updated
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal
