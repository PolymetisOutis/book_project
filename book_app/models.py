from django.db import models

# Create your models here.

class LargeCategory(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class SmallCategory(models.Model):
    large_category = models.ForeignKey(LargeCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Books(models.Model):
    category = models.ForeignKey(SmallCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    order = models.PositiveSmallIntegerField(null=True, blank=True)

