from django.core import paginator
from django.shortcuts import get_object_or_404, render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.core.paginator import Paginator


@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')

    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        # 'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_safe
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
        'page_name': 'CREATE',
    }
    return render(request, 'articles/forms.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
        'page_name': 'UPDATE',
    }
    return render(request, 'articles/forms.html', context)


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')
