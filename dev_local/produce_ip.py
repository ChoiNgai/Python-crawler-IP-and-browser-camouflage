import random

def create_ip_file(filename):
    ips = ['172.25.254.' + str(i) for i in range(1,255)]
    print(ips)
    with open(filename,'a+') as f:
        for count in range(1200):
            print(random.sample(ips,1))  #从列表中随机获取一个元素
            f.write(random.sample(ips,1)[0] + '\n')

create_ip_file('ips.txt')
