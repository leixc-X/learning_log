#### 项目介绍
使用python的Django框架搭建的web应用程序，前端框架选择的是django-bootstrap3，数据库SQLite
项目名为 学习博客（learning_log）
用户可以注册登录，并记录自己的学习笔记

######环境依赖
python 3.7
Django 2.0及以上版本
数据库：SQLite(Django自带数据库)



######部署步骤
1. 下载项目

2. cmd进入命令模式，进入文件目录 启动虚拟环境 ll_env\Scripts\activate

3. 进入虚拟环境后输入 python manage.py runserver启动服务器
4. 浏览器输入地址即可
5. 如果需要数据库迁移可以在命令行输入python manage.py makemigrations  
	记录改动输入python manage.py migrate  迁移数据到数据库
	python manage.py createsuperuser 迁移数据到数据库





###########目录结构描述
├── Readme.md                   // help
├── learning_log                   //项目配置文件
├── learning_logs					//项目应用文件
│   ├── migrations				//数据库文件
│   ├── templations            // html文件夹
├── ll_env 							//创建虚拟环境
├── users                         // 登录注册应用程序
├── db.sqlites					//数据库文件
├── manage.py
