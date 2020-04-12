from utils import log
from models import Message
from models import User

import random

# 这个函数用来保存所有的 messages
message_list = []
# session 可以在服务器端实现过期功能
session = {}


def random_str():
    """
    生成一个随机的字符串
    """
    seed = 'abcdefjsad89234hdsfkljasdkjghigaksldf89weru'
    s = ''
    for i in range(16):
        # 这里 len(seed) - 2 是因为我懒得去翻文档来确定边界了
        random_index = random.randint(0, len(seed) - 2)
        s += seed[random_index]
    return s


def template(name):
    """
    根据名字读取 templates 文件夹里的一个文件并返回
    """
    path = 'templates/' + name
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def current_user(request):
    session_id = request.cookies.get('user', '')
    username = session.get(session_id, '【游客】')
    # username = request.cookies.get('user', '【游客】')
    return username


def route_index(request):
    """
    主页的处理函数, 返回主页的响应
    """
    header = 'HTTP/1.1 210 VERY OK\r\nContent-Type: text/html\r\n'
    body = template('index.html')
    username = current_user(request)
    body = body.replace('{{username}}', username)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def response_with_headers(headers, code=200):
    """
    Content-Type: text/html
    Set-Cookie: user=gua
    """
    header = 'HTTP/1.1 {} VERY OK\r\n'.format(code)
    header += ''.join(['{}: {}\r\n'.format(k, v)
                       for k, v in headers.items()])
    return header


def redirect(url):
    """
    浏览器在收到 302 响应的时候
    会自动在 HTTP header 里面找 Location 字段并获取一个 url
    然后自动请求新的 url
    """
    headers = {
        'Location': url,
    }
    # 增加 Location 字段并生成 HTTP 响应返回
    # 注意, 没有 HTTP body 部分
    r = response_with_headers(headers, 302) + '\r\n'
    return r.encode('utf-8')


"""
HTTP/1.1 302 xxx
Location: /

"""


def route_login(request):
    """
    登录页面的路由函数
    """
    headers = {
        'Content-Type': 'text/html',
        # 'Set-Cookie': 'height=169; gua=1; pwd=2; Path=/',
    }
    # log('login, headers', request.headers)
    log('login, cookies', request.cookies)
    username = current_user(request)
    if request.method == 'POST':
        form = request.form()
        u = User.new(form)
        if u.validate_login():
            # 设置一个随机字符串来当令牌使用
            session_id = random_str()
            session[session_id] = u.username
            headers['Set-Cookie'] = 'user={}'.format(session_id)
            # 下面是把用户名存入 cookie 中
            # headers['Set-Cookie'] = 'user={}'.format(u.username)
            result = '登录成功'
        else:
            result = '用户名或者密码错误'
    else:
        result = ''
    body = template('login.html')
    body = body.replace('{{result}}', result)
    body = body.replace('{{username}}', username)
    header = response_with_headers(headers)
    r = header + '\r\n' + body
    log('login 的响应', r)
    return r.encode(encoding='utf-8')


def route_register(request):
    """
    注册页面的路由函数
    """
    header = 'HTTP/1.1 210 VERY OK\r\nContent-Type: text/html\r\n'
    if request.method == 'POST':
        form = request.form()
        u = User.new(form)
        if u.validate_register():
            u.save()
            result = '注册成功<br> <pre>{}</pre>'.format(User.all())
        else:
            result = '用户名或者密码长度必须大于2'
    else:
        result = ''
    body = template('register.html')
    body = body.replace('{{result}}', result)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def route_message(request):
    """
    消息页面的路由函数
    """
    username = current_user(request)
    # 如果是未登录的用户, 重定向到 '/'+
    if username == '【游客】':
        log("**debug, route msg 未登录")
        return redirect('/')
    log('本次请求的 method', request.method)
    if request.method == 'POST':
        form = request.form()
        msg = Message.new(form)
        log('post', form)
        message_list.append(msg)
        # 应该在这里保存 message_list
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    # body = '<h1>消息版</h1>'
    body = template('html_basic.html')
    msgs = '<br>'.join([str(m) for m in message_list])
    body = body.replace('{{messages}}', msgs)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def route_static(request):
    """
    静态资源的处理函数, 读取图片并生成响应返回
    """
    filename = request.query.get('file', 'doge.gif')
    path = 'static/' + filename
    with open(path, 'rb') as f:
        header = b'HTTP/1.1 200 OK\r\nContent-Type: image/gif\r\n\r\n'
        img = header + f.read()
        return img


'''
5, 增加一个路由 /admin/users
只有 id 为 1 的用户可以访问这个页面, 其他用户访问会定向到 /login
这个页面显示了所有的用户 包括 id username password
6, 在 /admin/users 页面中新增一个表单
表单包括 id password 两个 input
管理员可以在这个表单中输入 id 和 新密码 来修改相应用户的密码
这个表单发送 POST 请求到 /admin/user/update
所以你要增加一个新的路由函数实现更新用户密码的功能
'''


def route_admin(request):
    log('debug route_admin in')
    username = current_user(request)
    log('username', username)
    u = User.find_by(username=username)
    log('u', u)
    if u is None or u.role != 1:
        return redirect('/login')
    else:
        header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
        # body = '<h1>消息版</h1>'
        body = template('admin_user.html')
        r = header + '\r\n' + body
        return r.encode(encoding='utf-8')
    pass


def route_admin_update(request):
    # 你要增加一个新的路由函数实现更新用户密码的功能
    # 得到数据 解析数据  修改数据 保存数据
    username = current_user(request)
    u = User.find_by(username=username)
    if u is None or u.role != 1:
        return redirect('/login')
    if request.method == 'POST':
        # 修改并且保存 user
        form = request.form()
        id = int(form.get('id', -1))
        update_user = User.find_by(id=id)
        log('update_user', update_user)
        password = form.get('password', -1)
        update_user.password = password
        update_user.save()
    # 浏览器发送数据过来被处理后, 重定向到首页
    # 浏览器在请求新首页的时候, 就能看到新增的数据了
    return redirect('/admin/users')
    pass


# 路由字典
# key 是路由(路由就是 path)
# value 是路由处理函数(就是响应)
route_dict = {
    '/': route_index,
    '/login': route_login,
    '/register': route_register,
    '/messages': route_message,
     # admin
    '/admin/users': route_admin,
    '/admin/user/update': route_admin_update,
}
