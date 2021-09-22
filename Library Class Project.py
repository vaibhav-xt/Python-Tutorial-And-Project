# add book
# display book
# lend book
# return book
import configparser

with open("lendbook.txt", "a") as f:
    f.close()

class Library():

    def listofbooks(self):
        no = 1
        with open("Library Book.txt") as f:
            for i in f:
                print(f"{no}. {i}\n")
                no += 1
        f.close()

    def addbook(self):
        global display_book
        add = input("Enter Name Of The Book: ")
        add = add.capitalize()
        with open("Library Book.txt", "a") as f:
            f.write(add)
        f.close()
        print("Book added Successfully\n")

    def lend(self):
        global display_book
        global dict_book
        input_book_name = input("Enter Book Name To Search In Library: ")
        input_book_name = input_book_name.capitalize()
        with open("Library Book.txt") as s:
            with open("lendbook.txt", "a+") as f:
                a = f.readlines()
                lib_dict = {}
                for line in a:
                    parsed = line.split("\t")
                    lib_dict[0] = parsed[1]
                if input_book_name == f.keys():
                    if input_book_name in s:
                        print("Yes Book present in Library. Want to lend a book if Yes then go for 'y' otherwise 'n'")
                        choice = input("Enter: ")
                        choicelist = ["y", "n"]
                        if choice.lower() in choicelist[0]:
                            inputname = input("Enter Book Name: ")
                            Your_Name = input("Enter Your Name: ")
                            Your_Name = Your_Name.capitalize()
                            inputname = inputname.capitalize()
                            if inputname in "Library Book.txt":
                                f.write(f"{inputname}:  {Your_Name}")
                            else:
                                print("Book Name Is InCorrect!")
                        elif choice.lower() == choicelist[1]:
                            library_program.lend()
                        else:
                            exit()
                elif input_book_name in f:
                    print(f"{input_book_name} is owned by {dict_book[input_book_name]}")
                    print("Want Any Other book \n")
                else:
                    print("Entered Book Name Is InValid!")


    def return_book(self):
        global display_book
        global dict_book
        input_user_name = input("Enter Your Name: ")
        if input_user_name in dict_book:
            dict_book.pop(input_user_name)
            print("Successfully Done!")
        else:
            print("Entered UserName Is InValid!")

while True:
    if __name__ == '__main__':
        print("    ** Human Library **")
        print("1. Display Book\n2. Add Book\n3. Lend Book\n4. Return Book\n5. Exit\n ")
        choice = int(input("Enter Your Choice: "))
        library_program = Library()
        if choice == 1:
            library_program.listofbooks()
        elif choice == 2:
            library_program.addbook()
        elif choice == 3:
            library_program.lend()
        elif choice == 4:
            library_program.return_book()
        elif choice == 5:
            exit()
        else:
            print("InValid!")

