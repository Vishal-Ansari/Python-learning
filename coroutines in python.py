def searcher():
    import time
    # some 4 seconds time consuminng task
    book="This is a book on vishal and story of vishal and good"
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print("your text is in the book")
        else:
            print("Text is not in the book")

search=searcher()
print("search started...")
next(search)
search.send("harry")
input("press any key\n")
search.send("vishal and")
input("press any key\n")
search.send("story btao ")
input("press any key\n")
search.send(" good")


search.close()