books = {
    "Book1":"Author1",
    "Book2":"Author2",
    "Book3":"Author3"
}
def find(title):
    for x in books:
        if x in books:
            return books[x]
print(find("Book1"))