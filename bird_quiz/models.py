from django.db import models
from django.core.validators import validate_comma_separated_integer_list


class Group(models.Model):
    name = models.CharField(max_length=140)

class Bird(models.Model):
    common_name = models.CharField(max_length=140)
    latin_name = models.CharField(max_length=140, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    bad_pics = models.CharField(max_length = 500, null=True, blank=True, validators=[validate_comma_separated_integer_list])

    def __str__(self):
        return self.common_name