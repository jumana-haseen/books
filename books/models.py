from django.db import models

class BooksApp(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    review=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    publisheddate=models.DateField()
    profile_pic=models.ImageField(upload_to="images",null=True,blank=True)

    


    def __str__(self):
        return self.name