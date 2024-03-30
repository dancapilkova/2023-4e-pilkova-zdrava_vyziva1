from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


DAY_TIME = (
    ("breakfast", "Breakfast"),
    ("snack", "Snack"),
    ("lunch", "Lunch"),
    ("dinner", "Dinner"),
)

CUISINE = (
    ("czech", "Czech"),
    ("slovak", "Slovak"),
    ("french", "French"),
    ("thai", "Thai"),
    ("italian", "Italian"),
    ("chinese", "Chinese"),
    ("indian", "Indian"),
    ("korean", "Korean"),
    ("vietnamese", "Vietnamese"),
    ("japanese", "Japanese"),
    ("other", "Other"),
)


class Recipe(models.Model):
    user = models.ForeignKey(User, related_name="creator", on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    ingredients = RichTextField(max_length=10000, null=False, blank=False)
    instructions = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="recipes/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    meal_type = models.CharField(max_length=50, choices=DAY_TIME, default="breakfast")
    cuisine_types = models.CharField(max_length=50, choices=CUISINE, default="czech")
    calories = models.IntegerField()
    posted_date = models.DateTimeField(auto_now=True)

    class Order:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)
