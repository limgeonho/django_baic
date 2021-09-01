from django.db import models

"""
1. 모델명(클래스명) => 명사형 단수로 작성
2. 1 모델 == DB의 1 테이블과 대응(Article == excel에서 1 sheet)
3. 모델 클래스 내부의 클래스 변수 == 컬럼 이름에 해당
"""


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
