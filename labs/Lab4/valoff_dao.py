import requests
import json
import urllib.parse

url = "https://api.valoff.ie/api/Property/GetProperties"

parametrsAsDict = {
    "Download": "false",
    "Format": "json",
    "CategorySelected": "OFFICE",
    "LocalAuthority": "KERRY COUNTY COUNCIL",
    "Fields": "LocalAuthority,Category,Level,AreaPerFloor,NavTotal,CarPark,PropertyNumber,Use,FloorUse,Address,Eircode,PublicationDate"
}


def getAll():
    parametrs = urllib.parse.urlencode(parametrsAsDict)
    # print(parametrs)
    fullUrl = url + '?' + parametrs
    response = requests.get(fullUrl)

    return response.json()


if __name__ == "__main__":
    with open("labs\Lab4\\valloff.json", "wt") as fp:
        print(json.dumps(getAll()), file=fp)
