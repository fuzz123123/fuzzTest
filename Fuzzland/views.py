from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("<h1>Hello world !</h1>")


def get_temp(request):
    if request.method == 'GET':
        return render(request, 'test.html')
    elif request.method == 'POST':
        a = request.POST['num_a']
        b = request.POST['num_b']
        op = request.POST['op']
        req_dict = {
            "value_a": a,
            "value_b": b,
            "op": op,
            "result": get_tempt_res(int(a), op, int(b))
        }
        return render(request, 'test.html', req_dict)


def get_tempt_res(x, op, y):
    if op == '0':
        return x + y
    elif op == '1':
        return x - y
    elif op == '2':
        return x*y
    elif op == '3':
        return x/y
    else:
        return


def get_if_for(request):
    req_dict = {
        'a': 10
    }
    return render(request, 'test2.html', req_dict)


def get_img(request):
    return render(request, 'imagetest.html')


def play_with_cookies(request):
    response = HttpResponse()
    response.set_cookie(key="dj", value="wei in the house new", max_age=60*10)
    response.set_cookie(key="sessionid", value="951120", max_age=60*10)
    response.content = "123"
    return response
