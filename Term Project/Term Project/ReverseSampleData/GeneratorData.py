# Integer Data Generator
# @author: Chayapol Moemeng 
import random
import csv
import sys

def dataGenerator(dataSize,outputfile):
    with open(outputfile, 'w', newline='') as csvfile:
        wr = csv.writer(csvfile,delimiter=",")
        for x in range(dataSize,0,-1):
            wr.writerow([x])

if __name__ == "__main__":
    try:
        dataGenerator(int(sys.argv[1]),sys.argv[2])
    except (IndexError, ValueError):
        print('usage: %s <data size> [outputfile]' % sys.argv[0])
