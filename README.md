# v2ray-Management-web
【前端】轻量级，管理v2ray服务端流量消耗，用户端

# 管理端
下载Client.py文件，使用python运行即可 \
切记更改密钥和IP地址 \
如果自己电脑没有python环境或者想使用打包运行。将代码Fork自己仓库下，修改Client.py里面的服务器IP和密钥，使用GitHub Actions 进行编译打包后下载，直接双击运行即可。

# 用户端WEB
下载其它所有代码到服务端所在目录下，输入
```
gunicorn --reload -w 1 -b 0.0.0.0:5001 web:app
```
然后访问IP:5001 即可
