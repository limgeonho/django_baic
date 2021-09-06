from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm


def new(request):
    # <form> 내부의 HTML 만들기
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


def create(request):
    form = ArticleForm(request.POST)
    # 데이터 검증(+ HTML)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {
            'form': form,
        }
        return render(request, 'articles/new.html', context)


def index(request):
    pass


def detail(request, pk):
    pass