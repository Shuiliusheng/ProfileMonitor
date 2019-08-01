#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
import os
from email.mime.text import MIMEText
from email.utils import formataddr
 
my_sender='zhangtianxu@sjtu.edu.cn'    # 发件人邮箱账号
my_pass =os.environ['EMAIL_PASSWD']               # 发件人邮箱密码
xiayubin = 'xiayubin@gmail.com'
ipadstrust = 'ipads-trust@googlegroups.com'
user = '576781512@qq.com'
user2 = 'hanerzamora@gmail.com'


def mail():
    ret=True
    try:
        f = open("/home/ztx/follower/TargetArearHtml/.diff/TotalDiff.html")
        html_data = f.read()
    except:
        print("read file error")
    finally:
        f.close()
    try:
        msg=MIMEText(html_data, 'html', 'utf-8')

        msg['From']=formataddr(["ZhangTianxu",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        #msg['To']=formataddr(["ipads-trust",ipadstrust])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To']=formataddr(["xiayubin",xiayubin])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To']=formataddr(["ipads-trust",ipadstrust])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="大佬学术动态"                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.sjtu.edu.cn", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        #server.sendmail(my_sender,[xiayubin,ipadstrust],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(my_sender,[user2],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
 
def main():
    ret=mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
if __name__ == '__main__':
    main()
