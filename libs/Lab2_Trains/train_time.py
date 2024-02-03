import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)

# check it works
# print(doc.toprettyxml())

# check connection get data
# with open("trainxml.xml", "w") as xmlfp:
#    doc.writexml(xmlfp)

dataList = []

objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName(
        "TrainCode").item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
    dataList.append(traincode)

with open('Lab2_Trains\week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(
        train_file, delimiter='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    train_writer.writerow(dataList)
