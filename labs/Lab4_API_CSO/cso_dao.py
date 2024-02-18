import requests
import json

urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlAnd = "/JSON-stat/2.0/en"


def getAllAsFile(dataset):
    with open("labs\Lab4_API_CSO\\cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)


def getAll(dataset):
    url = urlBegining + dataset + urlAnd
    response = requests.get(url)
    return response.json()


def getFormatedAsFile(dataset):
    with open("labs\Lab4_API_CSO\\cso_formated.json", "wt") as fp:
        print(json.dumps(getFormated(dataset)), file=fp)


def getFormated(dataset):
    data = getAll(dataset)
    ids = data['id']
    values = data['value']
    dimensions = data['dimension']
    sizes = data['size']
    valueCount = 0
    result = {}

    for dim0 in range(0, sizes[0]):
        currentId = ids[0]
        index = dimensions[currentId]["category"]["index"][dim0]
        lable0 = dimensions[currentId]["category"]["label"][index]
        result[lable0] = {}
        # print(lable0)
        for dim1 in range(0, sizes[1]):
            currentId = ids[1]
            index = dimensions[currentId]["category"]["index"][dim1]
            lable1 = dimensions[currentId]["category"]["label"][index]
            result[lable0][lable1] = {}
            # print("\t", lable1)
            for dim2 in range(0, sizes[2]):
                currentId = ids[2]
                index = dimensions[currentId]["category"]["index"][dim2]
                lable2 = dimensions[currentId]["category"]["label"][index]
                result[lable0][lable1][lable2] = {}
                # print("\t\t", lable)
                for dim3 in range(0, sizes[3]):
                    currentId = ids[3]
                    index = dimensions[currentId]["category"]["index"][dim3]
                    lable3 = dimensions[currentId]["category"]["label"][index]
                    result[lable0][lable1][lable2][lable3] = {}
                    # print("\t\t\t", lable, " ", values[valueCount])
                    valueCount += 1

    print(result)
    return result


if __name__ == "__main__":
    # getAllAsFile("FP001")
    getFormatedAsFile("FP001")
