from django.db import models


# Create your models here.
class Roster(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    position = models.CharField(max_length=50)
    contact_number = models.CharField(
        max_length=11, help_text="Enter your mobile number"
    )
    slug = models.SlugField(default="", null=False)
    date_time = models.DateTimeField(auto_now_add=True)

    # todo add user password

    # def __str__(self):
    #     return self.name

    def __eq__(self, other):
        return self.pk == other.pk
