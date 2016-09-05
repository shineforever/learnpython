from django.shortcuts import render

# Create your views here.


# 跨域jsonp实例：demo1
def demo1(request):
    return render(request, "demo1.html")


# 跨域jsonp实例：demo2
def demo2(request):
    return render(request, "demo2.html")


# 跨域jsonp实例：demo3
def demo3(request):
    return render(request, "demo3.html")
