import requests
import json

url = "http://andrewbeatty1.pythonanywhere.com/books"


def getAllBooks():
    response = requests.get(url)
    return response.json()


def getBookById(id):
    getUrl = url + "/" + str(id)
    response = requests.get(getUrl)
    return response.json()


def createBook(book):
    response = requests.post(url, json=book)
    return response.json()


def updateBook(id, bookdiff):
    updateUrl = url + "/" + str(id)
    response = requests.put(updateUrl, json=bookdiff)
    return response.json()


def deleteBook(id):
    deleteUrl = url + "/" + str(id)
    response = requests.delete(deleteUrl)
    return response.json()


if __name__ == "__main__":
    # print(getAllBooks())
    # print(getBookById(513))
    # print(deleteBook(78))
    bookCreateData = {
        "Author": "test",
        "Price": 3000,
        "Title": "My Book",
        "id": 79
    }
    # print(createBook(bookCreateData))
    bookUpdateData = {
        'Price': 10000000
    }
    # print(updateBook(1,bookUpdateData))
