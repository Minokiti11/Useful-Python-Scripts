import csv
import random
import glob
from helps import * 

def main():

    path = "word_folder"

    files = [i.split("/")[-1] for i in list(glob.glob("./{}/*".format(path)))]
    for index,file in zip(range(len(files)),files):
        print("{} : {}".format(index,file))

    file = files[int(input("Select file number : "))%len(files)]
    file = open("{}/{}".format(path,file),'r',encoding="utf-8")
    word = list(csv.reader(file))
    word = word[1::]
    file.close()
    print(len(word))


    start = 1
    end = len(word)-1

    start = int(input("START : "))-1
    end = int(input("END : "))
    mode  = input("Mode : ")

    word = word[start:end]

    if mode == "random":
        frequency = int(input("frequency : "))
        
        miss = frequency

        for i in range(frequency,0,-1):
            r =  random.randint(0, len(word)-1)
            miss = miss -1  if ask(word[r],str(i)+" , ") else  miss + 0

        
        print('\033[32m{}%\033[0m'.format(int(float(miss/frequency)*100)))

    else:


        while word:
            wrong = []
            for i in range(len(word)):
                
                if ask(word[i]):
                    wrong.append(i)

            word = [word[i] for i in range(len(word)) if i in wrong]


    print('\033[32m'+'finish'+'\033[0m')

main()