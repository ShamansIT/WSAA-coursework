from valoff_dao import getAll

data = getAll()
totalArea = 0

for entery in data:
    valuationReports = entery["ValuationReport"]
    for valuationReport in valuationReports:
        if valuationReport['FloorUse'] == 'WORKSHOP':
            print(valuationReport['Area'], "+",
                  ('{0:.2f}'.format(totalArea)), "=", end="")
            totalArea += valuationReport['Area']
            print('{0:.2f}'.format(totalArea))

print(totalArea)
