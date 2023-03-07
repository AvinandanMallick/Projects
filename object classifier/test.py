import cv2
from cvzone.ClassificationModule import Classifier
import csv
from tkinter import *


def bill(name, price):
    with open('bill.csv', 'r+') as f:
        myDataList = f.readline()
        namelist = []
        for line in myDataList:
            entry = line.split(',')
            namelist.append(entry[0])

        if name not in namelist:
            f.writelines(f'\n{name},{price}')


def runprg():
    cap = cv2.VideoCapture(0)
    myClassifier = Classifier('MyModel/keras_model.h5', 'MyModel/labels.txt')

    lista = [0, 0, 0, 0]
    price = [0, 100, 200, 300]
    w = 1

    while True:
        _, img = cap.read()
        predictions, index = myClassifier.getPrediction(img, scale=1)
        name = myClassifier.list_labels[index]
        if index == 0:
            w = 1
        elif index != 0:
            if w == 1:
                lista[index] = lista[index] + 1
                bill(name, price[index])
                w = 0
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        # print(list)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def show():
    global myLabel2, myLabel3, myLabel4, no
    no=0
    sumtotal = 0
    filepath = 'C:/Users/anish/Desktop/Classification/bill.csv'
    File = open(filepath)
    Reader = csv.reader(File)
    Data = list(Reader)

    for x in list(range(0, len(Data))):
        if x > 0:
            sumtotal = sumtotal + int(Data[x][1])
        printing = Data[x][0] + "\t\t" + Data[x][1]
        if x == 0 or x == len(Data) - 1:
            myLabel2 = Label(root, text=printing, font="Verdana 15 underline", bg="yellow", width="25")
            myLabel2.pack()
            no+=1
        else:
            myLabel3 = Label(root, text=printing, font="Verdana 15", bg="yellow", width="25")
            myLabel3.pack()
            no+=1
    printing = "Total\t\t" + str(sumtotal)
    myLabel4 = Label(root, text=printing, font="Verdana 15 underline", bg="yellow", width="25")
    myLabel4.pack()
    no+=1

def clearbill():
    myLabel2.pack_forget()
    myLabel4.pack_forget()
    myLabel3.pack_forget()

    ml = [('Item', 'Price')]
    for i in range(no-1):
        ml.append(None)

    f = open("bill.csv", "r+")
    csvw = csv.writer(f)
    csvw.writerows(ml)
    f.close()


root = Tk()
root.title('Automated Billing System')
root.geometry("400x600")

myLabel1 = Label(root, text="Automated Bill Generator", font=('Times', 24))
myLabel1.pack()

myLabel0 = Label(root, text="")
myLabel0.pack()

myButton1 = Button(root, text="Start", command=runprg, font=10)
myButton1.pack()

myLabel0 = Label(root, text="")
myLabel0.pack()

myButton2 = Button(root, text="Show Bill", command=show, font=10)
myButton2.pack()

myLabel0 = Label(root, text="")
myLabel0.pack()

myButton3 = Button(root, text="Clear", command=clearbill, font=10)
myButton3.pack()

myLabel0 = Label(root, text="")
myLabel0.pack()

root.mainloop()
