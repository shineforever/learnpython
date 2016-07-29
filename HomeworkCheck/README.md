学习委员（英文不知道咋写）
===


* author: liwenzhou
* version: 0.1



### 功能介绍
* 每周按照指定时间去检查指定目录下的作业提交情况
* 给没有交作业的同学发邮件提醒

### 环境依赖


### 目录结构
    HomeworkCheck
    ├── __init__.py
    ├── README.md
    ├── bin #入口程序目录
    │   ├── __init__.py
    │   └── HomeworkCheck.py #入口程序
    ├── conf #配置文件目录
    │   ├── __init__.py
    │   ├── action_registers.py #菜单注册文件
    │   └── setting.py #全局变量配置文件
    ├── core #程序核心目录
    │   ├── __init__.py
    │   ├── utils.py #yaml解析
    │   ├── mylogging.py #log配置文件
    │   └── views.py #功能核心
    ├── home #yaml配置文件目录
    │   ├── __init__.py
    │   ├── new_hostandsysuser.yaml
    │   └── new_hosts.yaml
    └── log #堡垒机程序日志目录
        ├── __init__.py
        └── StupidJumpServer.log #堡垒机程序日志


### 使用方法

