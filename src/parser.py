import math
import os
import random
import csv
from tqdm import tqdm
DATA_PATH = "data/"
STANFORD_DS_DIR = os.path.join(DATA_PATH,"stanford_ds")
STANFROD_ANNOTATIONS = os.path.join(STANFORD_DS_DIR,'Annotation')
STANFROD_IMAGES= os.path.join(STANFORD_DS_DIR,'Images')
OUTPUT_TRAIN = os.path.join(DATA_PATH,"train")
OUTPUT_TEST = os.path.join(DATA_PATH,"test")

print(STANFROD_IMAGES)
# creats an easy way to contain the sample values
class Sample:
    def __init__(self,fileName:str, value:str) -> None:
        self.fileName =  fileName # name does not contain the .jpg at the end
        self.value = value
        pass
    def printOut(self):
        print("File name: " + self.fileName + ", Value: " + self.value)
    
def convertImageNametoHexHash(name:str) -> str:
    # convertrs the name to a hash and returns it 
    imgHash:int = abs(name.__hash__())
    hexhHash = hex(imgHash)
    print(hexhHash[2:])
    return hexhHash[2:]

def getAllImages(dir:str) -> list:
    trainSamples = [] # training
    testSamples = [] # test validation
    pathsToCopyTest = []
    pathsToCopyTrain = []
    listOfImgDirs = os.listdir(dir)
    for directory in listOfImgDirs:
        value = directory.lower()[10:]
        imageDirectories = os.path.join(dir,directory)
        imagesNames = os.listdir(imageDirectories)
        for j in range(len(imagesNames)):#imageName in imagesNames:
             # gets the hex hash number for the image name
            s = Sample(imagesNames[j][:-4],value)
            if j < 10:
                # use these for testing
                pathsToCopyTest.append(os.path.join(imageDirectories,imagesNames[j]))
                testSamples.append(s)
            else:
                # use for training
                pathsToCopyTrain.append(os.path.join(imageDirectories,imagesNames[j]))
                trainSamples.append(s)
    # randomize the samples
    random.shuffle(trainSamples)
    random.shuffle(testSamples)
    copyToTargetDir(pathsToCopyTest, OUTPUT_TEST)
    copyToTargetDir(pathsToCopyTrain, OUTPUT_TRAIN)
    return trainSamples, testSamples




def printAll(samples:list):
    for s in samples:
        print(s.value)
def generateCSV(trainingS:list, testingS:list):
    # saves two files one for training and one for testing
    file = open(DATA_PATH + "labels.csv", 'w')
    writer = csv.writer(file)

    csvString = ["id","breed"]
    writer.writerow(csvString)
    for s in trainingS:
        stringToWrite = [s.fileName, s.value]
        writer.writerow(stringToWrite)
    file.close()
    ###################
    # for testing
    file = open(DATA_PATH + "testLabels.csv", 'w')
    writer = csv.writer(file)

    csvString = ["id","breed"]
    writer.writerow(csvString)
    for s in testingS:      
        stringToWrite = [s.fileName, s.value]
        writer.writerow(stringToWrite)
    file.close()

def copyToTargetDir(paths:list, output):
    print("Copy the files to " + output)
    for i in tqdm(range(len(paths))):
        os.system("cp " + paths[i] + " " + output)


def main():
    # generates the dataset
    trainSmaples,testSamples = getAllImages(STANFROD_IMAGES)
    generateCSV(trainingS=trainSmaples,testingS=testSamples) 

main()
