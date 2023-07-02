from django.db import models

class Whey(models.Model):
    name= models.CharField(max_length=200)
    brand_name= models.CharField(max_length=1000)
    protein_content_in_g= models.CharField(max_length=2)

    def __str__(self):
        return self.name+':'+ self.brand_name

