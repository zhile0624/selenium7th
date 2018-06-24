#这个文件是用来批量执行unittest的测试用例
#该文件是我们这个测试工具的唯一入口
#1.导入unitest,因为批量执行用例的功能由unittest代码库提供
import smtplib
import unittest
#生成测试报告
import os
from email.mime.text import MIMEText

from package.HTMLTestRunner import HTMLTestRunner
#1.通过path打开新生成的测试报告文件
# HTML格式不是文本格式，需要制定以二进制的方式打开
def send_email(path):
    file = open(path,'rb')
    #读取邮件内容作为邮件正文
    msg = file.read()
    #3.把读取出来的内容转换成MIMEText格式
    #邮件类型一般有三种：纯文本plain，html,富文本
    mime = MIMEText(msg, _subtype='html', _charset='utf-8')
    #4除了正文以外，还需要设计主题，还需要发件人收件人
    mime['Subject'] = '海盗商城测试报告'
    #因为发件人需要登录密码，这里的密码不是真正的密码，是客服端授权码 账号需要开通客户端授权码
    mime['From'] ='bwftest126@126.com'
    mime['To'] ='285059520@qq.com'
    #实现SMTP（）构造方法
    smtp = smtplib.SMTP
    smtp.connect("smtp.qq.com")
    smtp.login('bwftest126@126.com', 'abc123asd654')
    #sendmail
    smtp.send_message(msg, from_addr='bwftest126@126.com', to_addrs='285059520@qq.com')
    smtp.quit()
    print("邮件已发送")
if __name__ == '__main__':
    #2想批量执行，首先要明确你要执行那些测试用例
    #只能执行继承了unitest.TestCase的类
    #defaultTestLoader默认测试用例的加载器，可以用来发现所有的测试用例
    suite = unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    #3执行这些测试 用例
#    unittest.TextTestRunner().run(suite)
    #4生成测试报告
    base_path = os.path.dirname(__file__)
    path = base_path+'/report/test_report.html'
    #创建测试文件
    file = open(path,'wb')
    HTMLTestRunner(stream=file, verbosity=1, title="海盗商城测试报告", description="这是描述信息；测试环境sever2008；浏览器'Chrome'").run(suite)
    #发送测试报告
    send_email(path)
