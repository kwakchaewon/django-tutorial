from django.db import models

# Create your models here.

# DB에 대한 Model을 정의하며 테이블을 정의하고 관리한다.
# makemigrations: 바뀐 DB 구조를 확인한다.
# migrations: 바뀐 스키마를 DB에 반영한다.
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)