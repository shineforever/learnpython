# jsonp demo

- author:master@liwenzhou.com 

> 以Django框架为例，举例说明jsonp的原理及实现

`server端：jsonp_demo_django以127.0.0.1:8888启动`

`client端：jsonp_demo_client以127.0.0.1:8000启动`

通过分别访问client的demo1.html、demo2.html、demo3.html，模拟跨域操作，了解jsonp的原理及应用。

------

## demo组成
- 启动两个django程序（server端和client端），从客户端去访问服务端的数据，来模拟跨域
  - server端：jsonp_demo_django_server  localhost:8888
  - client端：client  localhost:8888

### demo1
最简单的跨域
跨域执行js脚本,demo1.js,alert一个提示信息
- server端：jsonp_demo_django/static/demo1.js
- client端：jsonp_demo_client/templates/demo1.html



### demo2
client端固定的JS,返回信息
- server端：jsonp_demo_django/static/demo2.js
- client端：jsonp_demo_client/templates/demo2.html


### demo3
client端动态url，返回信息
- server端：jsonp_demo_django/jsonp_demo_django_server/views.py和jsonp_demo_django/jsonp_demo_django/urls.py两个文件
- client端：jsonp_demo_client/templates/demo3.html

 
 
 参考链接：
 http://blog.csdn.net/ritsu_/article/details/50511479