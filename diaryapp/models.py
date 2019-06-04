from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True,blank=True) 
    created_at = models.DateTimeField(auto_now_add = True) # 만든 날짜
    updated_at = models.DateTimeField(auto_now = True) # 수정 날짜
    pic = models.ImageField(upload_to = 'images/',null=True) #사진 

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:20]
