"""
def searcher():
    import time
    # some time taking task
    book = "this is a book on vaibhav and Rexteria"
    time.sleep(3)

    while True:
        text = (yield )
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
next(search)
search.send("vaibhav")
input("press any key")
search.send("vaibhav")
search.close()
"""

def searchtxt():
    import time
    book = "akash harry haris carry amit ajey bhuvan shubham rahul aftab hrithik vivek ujjawal mohit rohit"
    time.sleep(5)

    while True:
        text = (yield)
        if text in book:
            print("Your name is in the file.")
        else:
            print("Your Name is not present in the file")


search = searchtxt()
next(search)
search.send("vaibhav")
search.close()
