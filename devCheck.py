import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
from ping3 import ping

def mail_creat():
    msg_from = '542283486@qq.com'   # 发送邮箱
    password = 'dshklzoutyyabfjg'   # 授权码
    msg_to = '542283486@qq.com'     # 收件邮箱
    subject = '网元监测'             # 邮件主题
    content = '网元监测'             # 邮件内容
    msg = MIMEText(content)         # 生成MIMEText对象
    msg['Subject'] = subject        # 放入邮件主题
    msg['From'] = formataddr(('监测机器人', msg_from))    # 放入发件人
    msg['to'] = msg_to

    s = smtplib.SMTP_SSL('smtp.qq.com', 465)
    s.login(msg_from, password)
    s.sendmail(msg_from, msg_to, msg.as_string())
mail_creat()
# def online_echo():
#     content = '持续监测中。。。'
#     time.sleep(10800)
#     return content
#
def ping_dev():
        l_unreached = []
        with open('网元IP.txt', 'r', encoding='utf-8') as f:
            for i in f.readlines():
                l_ip = i.split('	')
                ip = l_ip[0]
                dev = l_ip[1].strip('\n')
                # print(ip)
                # print(dev)
                res = ping(ip)
                if res:
                    pass
                else:
                    print(f'网元 {dev} 连接异常！')
                    l_unreached.append(ip)
                    print(l_unreached)
                    time.sleep(2)
                    for ip in l_unreached:
                        res_err = ping(ip)
                        # print(res_err)
                        if res_err:
                            print(f'网元 {dev} 连接恢复正常！')
                        else:
                            pass
#
# if __name__ == '__main__':
#     try:
#         while True:
#             mail_creat()


