# Health Management System
# 3 clients - Harry, Rohan and Hammad


client_list = []


def fetch_data():
    with open('Vaibhav.txt', 'rt') as ff:
        ff.read()
        eof = ff.tell()
        ff.seek(0)
        while (ff.tell() != eof):
            obj = str(ff.readline())
            len_obj = len(obj)
            obj = obj[0:len_obj - 1]
            client_list.append(obj)


def choice():
    print('Enter your choice:')
    print('1. Retrive\n2. Lock\n3. Exit\t')
    choice = int(input())
    cl_name = input('Enter you client name:\t')
    if (choice == 1):
        retreive_diet(cl_name)
    elif (choice == 2):
        lock_diet(cl_name)
    elif (choice == 3):
        save()
    else:
        print('You entered wrong choice')


def save():
    with open('Vaibhav.txt', 'w') as fp:
        for x in client_list:
            str_name = x
            str_name = str_name + '\n'
            fp.write(str_name)
    exit()


def getdate():
    import datetime
    return datetime.datetime.now()


def add_client(name):
    client_list.append(name)
    with open('Vaibhav.txt', 'a') as fp:
        for x in client_list:
            str_name = x
            str_name = str_name + '\n'
            fp.write(str_name)
    lock_diet(name)


def identify(name):
    # print('Enter the name of client:\t')
    # name = input()
    if name in client_list:
        return 1
    else:
        return -1


def retreive_diet(name):
    id = identify(name)
    if (id == 1):
        try:
            with open('{name}.txt', 'rt') as fp:
                print(fp.read())
        except Exception:
            print('File do not exist')
    else:
        ch = input('Named client data not found, Do you want to create a data: Press Y or N:\t')
        if (ch == 'y' or ch == 'Y'):
            add_client(name)
        else:
            choice()
    ch = input('Do you want to continue from menu or exit: Press Y or N:\t')
    if (ch == 'y' or ch == 'Y'):
        choice()
    else:
        exit()


def lock_diet(name):
    id = identify(name)
    if (id == 1):
        print('Enter the diet which you want to add in your list: \t')
        diet = input()
        diet = diet + '\n'
        date = str(getdate())
        date = date[0: 10]
        try:
            with open('{name}.txt', 'a') as fp:
                fp.write(date + ": " + diet)
        except Exception:
            print('File not found')
        print('Lock successfully')
    else:
        print('Client Data not found')
        ch = input('Do you want to create a data: Press Y or N: \t')
        if (ch == 'y' or ch == 'Y'):
            add_client(name)
        else:
            choice()
    ch = input('Do you want to continue from menu or exit: Press Y or N:\t')
    if (ch == 'y' or ch == 'Y'):
        choice()
    else:
        exit()


fetch_data()
choice()