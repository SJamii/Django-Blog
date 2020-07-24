from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    mobile_no = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name


class Posts(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    description = models.TextField()
    image = models.ImageField(blank=True,null=True,upload_to='post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title