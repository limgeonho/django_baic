from django.shortcuts import render
import random
from django.http.response import HttpResponse


# urls.py의 urlpattern안에 있는 'hello/<name>/'의 name변수명과 맞춰줘야한다. == variable routing
def hello(request, name):
    # 이름을 URL을 통해 받는다.
    # hello/geonho/
    context = {
        'name': name,
    }
    return render(request, 'first_app/hello.html', context)


def lunch(request):
    menus = ['백반', '샌드위치', '짜장면', '굶기']
    menu = random.choice(menus)
    html = f'<h1>{menu}</h1>'
    # render(request, html파일, context(dict))
    context = {
        'menu': menu,
        'name': 'geonho',
    }
    return render(request, 'first_app/lunch.html', context)


def lotto(request):
    numbers = list(range(1, 46))
    lotto_numbers = random.sample(numbers, 6)
    lotto_numbers.sort()
    context = {
        'lotto_numbers': lotto_numbers,
    }
    return render(request, 'first_app/lotto.html', context)


def ping(request):
    # 사용자에게 <form>이 담긴 HTML제공
    return render(request, 'first_app/ping.html')

# ping에서 <form>을 통해 보낸 데이터를 읽어서 pong.html로 보여주는 함수


def pong(request):
    # request에서 값을 꺼내기
    # print(request.GET)
    # <QueryDict: {'mesaage': ['dasd'], 'sign': ['dasd']}> => 딕셔너리처럼 사용가능

    message = request.GET.get('message')
    sign = request.GET.get('sign')

    context = {
        # request꾸러미에서 GET 딕셔너리처럼 행동하는 것의 key값인 message와 sign으로 값을 가져온다
        # 하지만 key가 없다면...? name="signaaaa" -> 키에러 -> 키에러를 방질 할 수 있는 .get활용
        # 'a': request.GET['message'],
        # 'b': request.GET['sign'],
        'message': message,
        'sign': sign,
    }

    return render(request, 'first_app/pong.html', context)
