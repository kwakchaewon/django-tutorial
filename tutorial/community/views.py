from django.shortcuts import render
from community.forms import *
# Create your views here.

# 게시글 작성: 저장버튼을 누르면 작성한 폼을 DB에 저장한다.
# 정상적으로 폼이 전달될 경우 DB에 저장 후 랜더링한다.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()

    return render(request, 'write.html', {'form':form})

# 게시글 조회: 작성한 모든 게시글 목록을 표기한다.
# Article의 모든 컬럼을 가져와 전달 후 랜더링한다.
def list(request):
    articleList = Article.objects.all()
    return render(request, 'list.html',{'articleList':articleList})

# 게시글 검색: 검색한 게시글을 표기한다.
# 해당 id를 가진 Article 조회 후 랜더링한다. 
def view(request, num="1"):
    article = Article.objects.get(id=num)
    return render(request, 'view.html',{'article':article})