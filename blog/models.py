from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profil_image = models.ImageField(upload_to="")
    
    
    
    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Category"
        
        verbose_name_plural = "Categories"
        
        
        
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username
    
    
        
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    keywords = models.CharField(max_length=240,null=True,blank=True)
    thumbnail = models.ImageField(upload_to="",null=True,blank=True)
    image_url = models.CharField(max_length=500,null=True,blank=True)
    overwiev = RichTextField()
    date = models.DateField(auto_now_add=True)
    content = RichTextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    published = models.BooleanField()
    
    
    def __str__(self):
        return self.slug