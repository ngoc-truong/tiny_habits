from django.db import models
from django.utils import timezone

# Create your models here.


class Aspiration(models.Model):
    """An aspiration data model which represent the user's goals which s/he wants to achieve.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(
        verbose_name="Date published", default=timezone.now)

    def __str__(self):
        return self.title


class Behavior(models.Model):
    """A behavior data model which represent behaviors.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()

    # Many to many relationship
    aspirations = models.ManyToManyField(Aspiration, related_name="behaviors")

    def __str__(self):
        return self.title
