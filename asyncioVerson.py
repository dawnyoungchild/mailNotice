import smtplib
import time
import datetime
import asyncio
from email.mime.text import MIMEText
from email.utils import formataddr
from ping3 import ping

msg_from = '542283486@qq.com'  # 发送邮箱
password = 'dshklzoutyyabfjg'  # 授权码
msg_to = '542283486@qq.com'  # 收件邮箱
subject = '网元监测'



async def online_echo():
    while True:
        now = time.localtime()
        content = f'{time.strftime("%Y-%m-%d %H:%M:%S", now)} 持续监测中......'  # 邮件内容
        msg = MIMEText(content)  # 生成MIMEText对象
        msg['Subject'] = subject  # 放入邮件主题
        msg['From'] = formataddr(('监测机器人', msg_from))  # 放入发件人
        msg['to'] = msg_to
        s = smtplib.SMTP_SSL('smtp.qq.com', 465)
        s.login(msg_from, password)
        s.sendmail(msg_from, msg_to, msg.as_string())
        await asyncio.sleep(3 * 60 * 60)

async def ping_dev():
    while True:
        await asyncio.sleep(3)
        l_unreached = []
        with open('DEV_IP.txt', 'r', encoding='utf-8') as f:
            for i in f.readlines():
                l_ip = i.split('	')
                ip = l_ip[0]
                dev = l_ip[1].strip('\n')
                # print(ip)
                # print(dev)
                res = ping(ip, timeout=10)
                if res:
                    # await asyncio.sleep(10)
                    pass
                else:
                    res_com = ping(ip, timeout=10)
                    if res_com:
                        pass
                    else:
                        now = time.localtime()
                        print(f'网元 {dev} 连接异常！')
                        content = f'{time.strftime("%Y-%m-%d %H:%M:%S", now)} 网元 {dev} 连接异常！'
                        msg = MIMEText(content)  # 生成MIMEText对象
                        msg['Subject'] = subject  # 放入邮件主题
                        msg['From'] = formataddr(('监测机器人', msg_from))  # 放入发件人
                        msg['to'] = msg_to
                        s = smtplib.SMTP_SSL('smtp.qq.com', 465)
                        s.login(msg_from, password)
                        s.sendmail(msg_from, msg_to, msg.as_string())
                        await asyncio.sleep(60)
                        l_unreached.append(ip)
                        print(l_unreached)
                        for ip in l_unreached:
                            res_err = ping(ip)
                            # print(res_err)
                            if res_err:
                                now = time.localtime()
                                print(f'网元 {dev} 连接恢复正常！')
                                content = f'{time.strftime("%Y-%m-%d %H:%M:%S", now)} 网元 {dev} 连接恢复正常！'
                                msg = MIMEText(content)  # 生成MIMEText对象
                                msg['Subject'] = subject  # 放入邮件主题
                                msg['From'] = formataddr(('监测机器人', msg_from))  # 放入发件人
                                msg['to'] = msg_to
                                s = smtplib.SMTP_SSL('smtp.qq.com', 465)
                                s.login(msg_from, password)
                                s.sendmail(msg_from, msg_to, msg.as_string())
                            else:
                                pass

async def main():
    online_echo_task = asyncio.create_task(online_echo())
    ping_dev_task = asyncio.create_task(ping_dev())
    await asyncio.gather(online_echo_task, ping_dev_task)

if __name__ == "__main__":
    asyncio.run(main())
