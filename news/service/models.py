from django.db import models
class service(models.Model):
    topic=models.CharField( max_length=50)
    image=models.ImageField(upload_to= 'shop/images' , height_field=None, width_field=None, max_length=None)
    writer=models.CharField( max_length=50)
    Date=models.DateField()
    Headline=models.CharField(max_length=100)
    info=models.TextField()









# Create your models here.
