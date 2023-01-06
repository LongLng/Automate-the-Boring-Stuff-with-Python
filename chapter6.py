#Table Printer
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    
    for i in range(len(tableData)):
        for x in tableData[i]:
            if colWidths[i] < len(x):
                colWidths[i] = len(x)
    
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidths[y]),end=',')
        print()
        x += 1


if __name__=='__main__':
    printTable(tableData)