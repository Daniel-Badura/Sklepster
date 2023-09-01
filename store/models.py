from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)

 # define irregular plural 
    class Meta: 
        verbose_name_plural = 'categories'


    def __str__(self): 
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField(blank = True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images/', default='')
    
   
    class Meta: 
        verbose_name_plural = 'products'
# define a name of the product displayed on the product list
    def __str__(self):

        return self.title