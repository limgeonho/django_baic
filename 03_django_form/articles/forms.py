from django import forms
from django.forms import fields
from .models import Article

class ArticleForm(forms.ModelForm):
    
    # Meta는 반드시 써줘야 한다 -> 연결하려는 Article   
    class Meta:
        # Article과 연결
        model = Article
        # fields / exclude는 모델의 필드에만 적용됨
        # fields = ('title, ...')
        
        # model의 모든 field를 가져와!
        fields = '__all__'