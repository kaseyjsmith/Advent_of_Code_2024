from os import stat
import re

def readFile(file):
    with open(file) as file:
        data = file.read()
    return data

def parse(data):
    # Part 2:
    # Split into substrings between do() and don't()
    # Assuming the start to be do()
    # collect mul statments in these strings and perform the same 
    # calc function
    doPattern = r"do\(\)(.*?)don't\(\)"
    doStatements = re.findall(doPattern, data)
    print(doStatements)

    for statements in doStatements:
        # print(statements)
        pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
        matchGroups = re.findall(pattern, statements)
        # print(matchGroups)

    return matchGroups

def calculate(tupList):
    total = 0
    for t in tupList:
        total += int(t[0]) * int(t[1]) 
    return total

if __name__ == '__main__':
    # add 'do()' at the beginning of the file for part 2
    data = 'do()' + readFile('puzzle.txt')
    matches = parse(data)
    print(len(matches))
    print(calculate(matches))
