import re


template_root = "./templates"


# ----------更新----------
# 用来存放url路由映射
# url_route = {
#   "/index.py": index_func,
#   "/center.py": center_func
# }

g_url_route = dict()

def route(url):
    def func1(func):
        # 添加键值对，key是需要访问的url，value是当这个url需要访问的时候，需要调用的函数引用
        g_url_route[url] = func
        def func2(file_name):
            return func(file_name)
        return func2
    return func1



def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    file_name = environ['PATH_INFO']
    '''  
    #  普通版使用if判断来确定路径（不使用装饰器路由）
    if file_name == "/index.py":
        return index(file_name)
    elif file_name == "/center.py":
        return center(file_name)
    else:
        return str(environ) + '==Hello world from a simple WSGI application!--->%s\n' % time.ctime()
    '''
    # ----------更新----------
    try:
        for url, call_func in g_url_route.items():
            print(url)
            ret = re.match(url, file_name)
            if ret:
                return call_func(file_name, url)
                break
        else:
            return "没有访问的页面--->%s" % file_name
    except Exception as ret:
        return "%s" % ret
    else:
        return str(environ) + '-----404--->%s\n'





@route(r'/index.html')
def index(file_name):
    """返回index.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()
        #  可以在此查询数据库，增加数据库中的数据
        return content

@route(r'/center.html')
def center(file_name):
    """返回center.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()
        #  可以在此查询数据库，增加数据库中的数据
        '''
        import pymysql
        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        sql = """select * from info;"""
        cursor.execute(sql)
        data_from_mysql = cursor.fetchall()
        cursor.close()
        db.close()

        content = re.sub(r"\{%content%\}", str(data_from_mysql), content)
        '''
        return content


@route(r"/update/(\d*)\.html")
def update(file_name, url):
    """显示 更新页面的内容"""
    try:
        template_file_name = template_root + "/update.html"
        f = open(template_file_name)
    except Exception as ret:
        return "%s,,,没有找到%s" % (ret, template_file_name)
    else:
        content = f.read()
        f.close()
        '''
        from urllib.parse import unquote,quote 
        # quote() 该方法可以将内容转化为URL编码的格式,URL中带有中文参数时,又是可能会导致乱码的问题,用这个方法可以将中文字符转化为URL编码
        #unquote() 它对应上面的方法, 可以进行URL解码
        # keyword = '壁纸'  
        # url = 'http://www.baidu.coms?wd='+quote(keyword)  #  'http://www.baidu.coms?wd=%E5%A3%81%E7%BA%B8'
        # print(url) 
        
        # url = 'http://www.baidu.coms?wd=%E5%A3%81%E7%BA%B8'  
        # print(unquote(url))  # http://www.baidu.coms?wd='壁纸'
        
        # stock_note_info = unquote(stock_note_info) 
        
        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        # 会出现sql注入，怎样修改呢？ 参数化
        sql = """update focus inner join info on focus.info_id=info.id set focus.note_info="%s" where info.code=%s;""" % (stock_note_info, stock_code)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        '''
        ret = re.match(url, file_name)
        if ret:
            stock_code = ret.group(1)

        # 将提取到的股票编码返回到浏览器中,以检查是否能够正确的提取url的数据
        return stock_code

