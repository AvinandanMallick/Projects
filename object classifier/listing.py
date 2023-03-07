import cv2
from cvzone.ClassificationModule import Classifier
from tkinter import *
from datetime import datetime

item=[]

def runprg():
    cap = cv2.VideoCapture(0)
    myClassifier = Classifier('MyModel/keras_model.h5', 'MyModel/labels.txt')
    price = [0, 100, 200, 300]
    w = 1

    def bill(name, price):
        cnt=0
        for i in range(0,len(item)):
            if item[i][0]==name:
                item[i][1]+=1
                item[i][2]+=price
                cnt=1
        if cnt==0:
            item.append([name,1,price])

    while True:
        _, img = cap.read()
        predictions, index = myClassifier.getPrediction(img, scale=1)
        name = myClassifier.list_labels[index]
        print(index,item)
        if (index == 0):
            w = 1
        elif (index > 0):
            if (w == 1):
                bill(name, price[index])
                w = 0
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def show():
    global myItemlabel1,myItemlabel2,myItemlabel3
    print(item)
    sumprice=0
    for i in range(0, len(item)):
        sumprice+=item[i][2]
    item.insert(0,['Item','Quantity','Price'])
    item.append(['Total','',sumprice])
    printing=''
    for i in range(1,len(item)-1):
        printing += item[i][0] + '\t' + str(item[i][1]) + '\t' + str(item[i][2]) +'\n'

    myItemlabel1 = Label(root, text='Item\tQuantity\tPrice', font="Verdana 15 underline", bg="yellow")
    myItemlabel1.pack(fill=X)

    myItemlabel2 = Label(root, text=printing, font="Verdana 15", bg="yellow")
    myItemlabel2.pack(fill=X)

    myItemlabel3 = Label(root, text='Total\t=\t'+str(sumprice), font="Verdana 15 bold", bg="yellow")
    myItemlabel3.pack(fill=X)

    myButton2['state']=DISABLED
    myButton3['state'] = NORMAL

    with open('bill.csv', 'r+') as f:
        myDataList = f.readline()
        for line in myDataList:
            entry = line.split(',')
        now = datetime.now()
        date=now.strftime("%d.%m.%Y")
        time=now.strftime("%I:%M %p")
        f.writelines(f'\n{"Date"},{date},{"Time"},{time}')
        for i in range(0, len(item)):
            f.writelines(f'\n{item[i][0]},{item[i][1]},{item[i][2]}')

        f.writelines(f'\n')


def clearbill():
    del item[:]
    myButton2['state']=NORMAL
    myButton3['state'] = DISABLED
    myItemlabel1.destroy()
    myItemlabel2.destroy()
    myItemlabel3.destroy()



root = Tk()
root.title('Automated Billing System')
root.geometry("400x600")

myLabel1 = Label(root, text="Automated Bill Generator", font=('Times', 24))
myLabel1.pack()

myLabel0 = Label(root, text="")
myLabel0.pack()

myButton1 = Button(root, text="SCAN", command=runprg, font=10)
myButton1.pack()

myLabel0 = Label(root, text="")
myLabel0.pack()

myButton2 = Button(root, text="Show Bill", command=show, font=10)
myButton2.pack()

myLabel0 = Label(root, text="")
myLabel0.pack()

myButton3 = Button(root, text="Clear", command=clearbill, font=10)
myButton3.pack()
myButton3['state'] = DISABLED

myLabel0 = Label(root, text="")
myLabel0.pack()

myButton4 = Button(root, text="Close", command=root.destroy, font=10)
myButton4.pack()

myLabel0 = Label(root, text="")
myLabel0.pack()

root.mainloop()