def number_last_six_number():
    file_write_obj = open("male_idcard_lastsixnumber_data.txt","w+")
    print("open")
    for day in range(1, 31, 1):
        for lastthree_number in range(1, 999, 2):
        # for lastthree_number in range(1, 999, 2): female id card last six number
            for last_number in range(0, 9, 1):
                number = ("%02d" % day) + ("%03d" % lastthree_number) + ("%01d" % last_number)  + "\n"
                file_write_obj.write(number)
    file_write_obj.close();
    print("close")

if __name__=="__main__":
    print("main")
    number_last_six_number()
