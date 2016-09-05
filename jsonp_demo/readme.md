# jsonp demo

> 以Django框架为例，举例说明jsonp的原理及实现

------

## demo组成
- 启动两个django程序（server端和client端），从客户端去访问服务端的数据，来模拟跨域
  - server端：jsonp_demo_django_server  localhost:8888
  - client端：client  localhost:8888

### demo1
最简单的跨域
跨域执行js脚本,demo1.js,alert一个提示信息



### demo2
client端固定的JS,返回信息



### demo3
client端动态JS，返回信息


 
 
 参考链接：
 http://blog.csdn.net/ritsu_/article/details/50511479