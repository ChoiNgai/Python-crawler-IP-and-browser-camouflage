import os
import xlwt

#读取txt文件里的ip地址存储为列表
def ReadTxtName(rootdir):
    lines = []
    with open(rootdir, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)
    return lines


#保存列表
def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")

ip_list=ReadTxtName('ping1.txt')		#读取待判断是否有效的ip列表
Effective_ip = [ ]  #创建存储有效ip的列表

#判断ip是否可用
for i in range(3,len(ip_list)):
    result=os.system('ping '+ ip_list[i])   #0为可用ip，1为不可用ip
    #print("结果是",result)
    if result == 0:
        Effective_ip.append( ip_list[i])
    else:
        print("第"+str(i+1)+"个ip无效")

    text_save('ping713.txt', Effective_ip)
