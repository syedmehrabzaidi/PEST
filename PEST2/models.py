from django.db import models

# Create your models here.


# Create your models here.
class students(models.Model):
    pestname = models.CharField(max_length=60)
    croptype = models.CharField(max_length=60)

    tl = models.CharField(max_length=60)
    tu = models.CharField(max_length=60)
    dd = models.CharField(max_length=60)

    def __str__(self):
        return self.pestname