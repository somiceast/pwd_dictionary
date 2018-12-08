def number_last_six_number():
    file_write_obj = open(
        # "../output_data/female_idcard_lastsixnumber_data.txt", "w+") #female
        "../output_data/male_idcard_lastsixnumber_data.txt", "w+")
    print("open")
    for day in range(1, 32, 1):
        # for lastthree_number in range(0, 999, 2): #female
        for lastthree_number in range(1, 1000, 2):
            # number
            for last_number in range(0, 10, 1):
                number = ("%02d" % day) + ("%03d" %
                                           lastthree_number) + ("%01d" % last_number) + "\n"
                file_write_obj.write(number)
    file_write_obj.close()
    print("close")

if __name__ == "__main__":
    print("main")
    number_last_six_number()
