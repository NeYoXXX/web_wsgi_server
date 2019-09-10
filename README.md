# web_wsgi_server
自制web_wsgi_server

1.基本实现，文件架构

├── web_server.py  
├── web  
│   └── my_web.py  
└── html  
│       └── index.html

2.web框架

├── dynamic ---存放py模块  
│   └── my_web.py  
├── templates ---存放模板文件  
│   ├── center.html  
│   ├── index.html  
│   ├── location.html  
│   └── update.html  
├── static ---存放静态的资源文件  
└── web_server.py ---mini web服务器  

此项目为了学习和理解web框架原理和wsgi协议
