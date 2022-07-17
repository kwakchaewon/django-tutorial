from django.db import models

# Create your models here.

# DB에 대한 Model을 정의하며 테이블을 정의하고 관리한다.
# python manage.py makemigrations community: 테이블 생성
# python manage.py migrations: DB에 반영한다.
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)