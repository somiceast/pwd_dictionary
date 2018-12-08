import os

def number_last_six_number():
    for day in range(1, 31, 1):
        for lastfour_number in range(0, 9999, 20):
            number = ("%02d" % day) + ("%04d" % lastfour_number)
            file_write_obj.write(number)

def open_write():
    file_write_obj = open("data.txt","w+")
    print("open")

def close_write():
    file_write_obj.close();
    print("close")

if __name__=="__main__":
    k = raw_input("plz input:")
    print(k)
    print(os.path.isfile("data.txt"))
    day = 1
    lastfour_number = 3
    cwd=os.getcwd()
    print(cwd)

    # open_write();
    # number_last_six_number()
    # close_write();

    # print type("%02d" % day)
    # print "%04d" % lastfour_number
    # # number =  '%s%s%s' % (("%02d" % day), ("%05d" % lastfour_number))
    # print number
