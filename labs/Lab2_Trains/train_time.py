import requests
import csv
from xml.dom.minidom import parseString

retrieveTags = ['TrainStatus',
                'TrainLatitude',
                'TrainLongitude',
                'TrainCode',
                'TrainDate',
                'PublicMessage',
                'Direction'
                ]


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

# get and check trainCode start with
for objTrainPositionsNode in objTrainPositionsNodes:
    datanode = objTrainPositionsNode.getElementsByTagName(
        retrieveTags[3]).item(0)
    checkStartSymbol = datanode.firstChild.nodeValue.strip()
    if checkStartSymbol.startswith('D'):
        dataList.append(datanode.firstChild.nodeValue.strip())

# write data in file cvs
with open('Lab2_Trains\week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(
        train_file, delimiter='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    train_writer.writerow(dataList)
