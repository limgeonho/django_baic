from django.shortcuts import render
# Article에 접근하기 위해서는 models을 불러와야함
from .models import Article


# Create
def new(request):
    return render(request, 'articles/new.html')


def create(request):
    pass


# Read
def index(request):
    # 게시글들(articles) 불러오기 => DB에서 가져오기 => DB와 통식? => Model
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # 단일 게시글
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# Update


def edit(request, pk):
    pass


def update(request, pk):
    pass

# Delete


def delete(request, pk):
    pass
