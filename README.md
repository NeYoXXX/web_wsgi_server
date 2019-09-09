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
│   ├── css  
│   │   ├── bootstrap.min.css  
│   │   ├── main.css  
│   │   └── swiper.min.css  
│   └── js  
│       ├── a.js  
│       ├── bootstrap.min.js  
│       ├── jquery-1.12.4.js  
│       ├── jquery-1.12.4.min.js  
│       ├── jquery.animate-colors.js  
│       ├── jquery.animate-colors-min.js  
│       ├── jquery.cookie.js  
│       ├── jquery-ui.min.js  
│       ├── server.js  
│       ├── swiper.jquery.min.js  
│       ├── swiper.min.js  
│       └── zepto.min.js  
└── web_server.py ---mini web服务器  