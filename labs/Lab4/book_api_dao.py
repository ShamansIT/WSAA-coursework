import requests

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

    if response.status_code == 201:   # Check Created Status
        return response.json()
    elif response.status_code == 400:  # Check Bad Request Status
        return {'error': 'Invalid book data provided'}
    else:
        response.raise_for_status()  # Raise an exception for other errors


def updateBook(id, bookdiff):
    updateUrl = url + "/" + str(id)
    response = requests.put(updateUrl, json=bookdiff)
    return response.json()


def deleteBook(id):
    deleteUrl = url + "/" + str(id)
    response = requests.delete(deleteUrl)
    return response.json()


def readBooks(id):
    geturl = url + "/" + str(id)
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()  # Return the JSON data if successful
    elif response.status_code == 404:
        return {'error': 'Book not found'}  # Handle not found error
    else:
        response.raise_for_status()  # Raise an exception for other error


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
    print(readBooks())
