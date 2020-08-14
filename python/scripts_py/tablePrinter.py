#!/usr/local/bin/python3
# tablePrinter.py


def printTable(listOfLists):
    colWidths = []

    for index in range(len(listOfLists)):
        colWidths.append(len(max(listOfLists[index], key=len)))

    colMaxIndex = len(listOfLists)
    rowMaxIndex = len(listOfLists[0])

    for row in range(rowMaxIndex):
        for column in range(colMaxIndex):
            print(listOfLists[column][row].rjust(colWidths[column]), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
