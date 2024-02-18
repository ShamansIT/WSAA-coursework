import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

response = requests.get(url)


def getAll():
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve the dataset.")


def getAllAsFile():
    with open("assignments\Assignment_Exchequer_Account\\cso.json", "wt") as fp:
        print(json.dumps(getAll()), file=fp)


def printInfo():
    with open("assignments\Assignment_Exchequer_Account\\cso.json", "r") as file:
        data = json.load(file)
    # Accessing economic indicators
    economic_data = data['dimension']['STATISTIC']['category']['label']
    # Print economic indicators
    print("\nEconomic Indicators:")
    for key, value in economic_data.items():
        print(f"{key}: {value}")

    # Accessing financial indicators
    financial_data = data['dimension']['C02568V03113']['category']['label']
    print("\nFinancial Indicators:")
    for key, value in financial_data.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    getAllAsFile()
    printInfo()
