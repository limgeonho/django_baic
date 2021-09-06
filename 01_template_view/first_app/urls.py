from django.urls import path
from . import views

# html에서 {% url 'lotto' %}처럼 url을 불러올때 같은 lotto라는 url name이 존재하면 뭔지 모름... -> app_name을 설정하고 {% url 'first_app:lotto' %}로 불러온다.
# 따라서 app_name은 반드시 작성 -> html에서 url을 부를땐 {% url '<app_name>:<path안에 있는 name>' %}
app_name = 'first_app'

urlpatterns = [
    # first_app/ + hello
    # url안에 <>처리를 하면 <>안은 변수 처리된다.
    # 3번째 인자 == url의 변수명 -> html에서 name에 해당하는 url을 알아서 a태그로 불러온다 -> 앞으로 계속 path의 3번째 인자인 name을 활용!
    path('hello/<name>/', views.hello, name='hello'),
    path('lunch/', views.lunch, name='lunch'),
    path('lotto/', views.lotto, name='lotto'),
    path('ping/', views.ping, name='ping'),
    path('pong/', views.pong, name='pong'),

]
