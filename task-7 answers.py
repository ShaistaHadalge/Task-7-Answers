###Write a python program using Function for which will do the following.
###1.The function will create a text file with current timestamp.
###2. The file content should have the content of the current timestamp.

import datetime
def createfile():
    CurrTime = datetime.datetime.now()
    print(CurrTime)
    with open("timenow.txt",'w') as file:
        file.write(str(CurrTime))

createfile()


###Write another python function to read from a text file.The function will take the name of the
###textfile and display the content of the file into the console.
file = open("timenow.txt","r")
print(file.read())
file.close()


