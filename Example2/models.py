from django.db import models

# Create your models here.
class Example2(models.Model):
    name = models.CharField(max_length= 255, null = False)

    def __str__(self):
        return self.name
    
    class Meta:

        db_table = 'Example2'