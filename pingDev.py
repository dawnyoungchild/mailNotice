import time
from ping3 import ping

def ping_dev():
    while True:
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

ping_dev()