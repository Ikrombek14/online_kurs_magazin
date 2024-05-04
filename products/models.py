from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'
    def __str__(self):
        return self.name
class Products(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body=models.TextField()
    price = models.IntegerField()

    class Meta:
        db_table = 'products'
        
    def __str__(self):  
        return self.name


