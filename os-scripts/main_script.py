
#sys
# https://docs.python.org/3/library/sys.html

#os
#https://docs.python.org/3/library/os.html




def read_file_line_by_line(file_name):
    my_file = open(file_name)
    file_lines = my_file.readlines()
    for line in file_lines:
        line = line[0:len(line) - 1]#to cut the : /n
        print(line)

    my_file.close()



def main():
    print('main_script.py')


if __name__ == "__main__":
    main()