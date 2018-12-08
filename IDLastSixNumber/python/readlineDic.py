# coding:utf-8
import re


def read():
    file_write_obj = open("../output_data/pwd_163mail.txt", "w+")
    file = open("../read_data/163mail.txt")
    i = 1
    for line in file:
        # print(line)
        i = i + 1
        a = re.findall((re.compile(r'    (.+$)')), line)
        if a:
            pwd = a[0]
        else:
            ba = re.findall((re.compile(r'----(.+$)')), line)
            if ba:
                pwd = ba[0]
            else:
                ca = re.findall((re.compile(r'密：(.+$)')), line)
                if ca:
                    pwd = ca[0]
                else:
                    print(ca)
                    print i
                    pwd = None
                    continue
        file_write_obj.write(pwd + '\n')
    file_write_obj.close()


if __name__ == "__main__":
    read()
    # file = open("../read_data/163mail.txt")
    # c = file.readline().strip()
    # c = "hrn2000@163.com----[hyc1999999]"
    # d = "卡密：7758521 "
    # #     .+?$
    #     # pwd=re.findall((re.compile(r'\s\S.+?\s')),c)
    # pwd = (re.findall((re.compile(r'    (.+$)')), c))
    # pwd = (re.findall((re.compile(r'卡密：(.+$)')), d))
    # if pwd:
    # print("sth")
    # else:
    # print("none")
    # print(pwd)
    # file_write_obj = open("../read_data/pwd_163mail.txt","w+")

    # file_write_obj.write(pwd)

    print("123")
