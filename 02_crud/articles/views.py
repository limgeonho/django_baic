from django.shortcuts import render, redirect
# Article에 접근하기 위해서는 models을 불러와야함
from .models import Article


# Create
# 사용자에게 <form> 포함한 html을 전송(ping)
def new(request):
    return render(request, 'articles/new.html')


# 사용자가 제출한 데이터를 저장 => 상세 페이지로 이동
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    # context = {
    #     'article': article,
    # }
    # return render(request, 'articles/~', context)를 사용하지 않는 이유?
    # -> 사용자가 입력한 데이터를 DB에 저장했는데 이를 새로운 url페이지가 아닌 기존의 detail페이지에
    # pk값만 가지고 바로 전달!! == redirect

    # return redirect(f'/articles/{article.pk}') -> hardtyping보다는 아래의
    # -> redirect('articles:detail', article.pk) 이용
    # {% url 'articles:detail' article.pk %}와 같은 의미지만 다른 양식임!!!(주의)
    return redirect('articles:detail', article.pk)


# Read
# 전체 게시글 목록 조회
def index(request):
    # 게시글들(articles) 불러오기 => DB에서 가져오기 => DB와 통식? => Model
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# 특정 게시글 상세 조회
def detail(request, pk):
    # 단일 게시글
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# Update
# 사용자에게 <form>을 포함한 html전송(+내용 채워서)
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


# 사용자가 수정한 데이터를 저장(새로운 객체 만들기가 아니라 덮어써야함 -> pk로 해당 article를 불러와서 덮어쓰고 save()!!!) => 상세페이지로 이동
def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)


# Delete
# 특정 게시글을 삭제 => 목록페이지로 redirect
def delete(request, pk):
    article = Article.objects.get(pk=pk)

    # 사용자가 페이지에서 버튼을 누르는 것 == POST요청 -> POST요청이 들어왔을 경우에만 삭제 기능 활성화
    # 이런 처리를 하지 않으면 url로 접근해서(GET) 무작위로 삭제 가능(방어)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    # POST로 요청이 들어온 것이 아니라면 그냥 detail페이지로 redirect(=GET요청이면 방어)
    else:
        return redirect('articles:detail', article.pk)
