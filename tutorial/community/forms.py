from django.forms import ModelForm
from community.models import *

# Article이란 모델을 이용하여 폼을 만들고 표기할 컬럼을 나열한다.
class Form(ModelForm):
    class Meta:
        model = Article
        fields=['name', 'title', 'contents', 'url', 'email']