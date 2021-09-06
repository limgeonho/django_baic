from django.contrib import admin
from .models import Article

# Register your models here.
# 관리자 페이지에 Article를 등록하겠습니다!
admin.site.register(Article)
