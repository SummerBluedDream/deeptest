#模拟微博登录，先读取登录的邮箱和口令，然后按照 weibo.cn的登录页的格式以 username=xxx&password=xxx 的编码传入
from urllib import request, parse
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([('username', email),('password', passwd),('entry', 'mweibo'),('client_id', ''),('savestate', '1'),('ec', ''),('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')])
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0Mobile/10A5376e Safari/8536.25')
req.add_header('Referer','https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
for k, v in f.getheaders():
    print('%s: %s' % (k, v))
print('Data:', f.read().decode('utf-8'))

