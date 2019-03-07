from django.db import models
from imagekit.models import ImageSpecField #썸네일 만듦
from imagekit.processors import ResizeToFill # 크기 조정 쉽게 할 수 있음

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summery(self):
        return self.body[:100]

class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="blogimg")
    image_thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(120, 100)], format= 'JPEG', options= {'quality':60}) # source는 지정을 해주는 과정/ 확장자, 압축방식
