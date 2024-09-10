import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
from ping3 import ping

try:
    while True:
        msg_from = '542283486@qq.com'  # 发送邮箱
        password = 'dshklzoutyyabfjg'  # 授权码
        msg_to = '542283486@qq.com'  # 收件邮箱
        subject = '网元监测'  # 邮件主题
        content = '持续监测中......'  # 邮件内容
        msg = MIMEText(content)  # 生成MIMEText对象
        msg['Subject'] = subject  # 放入邮件主题
        msg['From'] = formataddr(('监测机器人', msg_from))  # 放入发件人
        msg['to'] = msg_to

        s = smtplib.SMTP_SSL('smtp.qq.com', 465)
        s.login(msg_from, password)
        s.sendmail(msg_from, msg_to, msg.as_string())
        time.sleep(10800)
except:
    pass
