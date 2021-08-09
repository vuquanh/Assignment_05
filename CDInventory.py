#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# AnhVu, 2021-Aug-06, Added Code
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstdict = []  # list of lists to hold data
dict3 = {} # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print ('[l] Load Inventory from file')
    print ('[a] Add CD\n[i] Display Current Inventory')
    print ('[d] Delete CD from Inventory')
    print ('[s] Save Inventory to file')
    print ('[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input

    # 1. Load inventory if the user chooses so 
    if strChoice == 'l':
        f = open ('CDInventory.txt', 'r')
        i = 0
        l = f.readlines ()
        while i < len(l) - 1:
            ID = l[i]
            ID = ID.replace('\n', '')
            Title = l[i+1]
            Title = Title.replace('\n', '')
            Artist= l[i+2]
            Artist= Artist.replace('\n', '')
            dict = {'ID':ID, 'Artist':Artist, 'Title': Title}
            lstdict.append (dict)  
            i = i + 3
        f.close ()
        pass
    
    # 2. Add CD if the user chooses so
    elif strChoice == 'a':  
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dict3 = {'ID': strID, 'Title': strTitle, 'Artist': strArtist}
        lstdict.append(dict3)
        pass
        
    # 3. Display the current data to the user each time the user wants to display the data 
    elif strChoice == 'i':
        print('ID, CD Title, Artist')
        for row in (lstdict):
            print(row)
        pass
            
    # 4. Deleting an entry if user chooses to do so
    elif strChoice == 'd':
        removeTitle = input ('Enter Title to be removed: ')
        for row in lstdict:
            Title1 =row ['Title']
            if Title1 == removeTitle:
                lstdict.remove (row)
        print ('New inventory is: ','\n',lstdict)
        pass
   
    # 5. Save the data to a text file CDInventory.txt if the user chooses so 
    elif strChoice == 's': 
        for row in lstdict:
            print (row)
            ID1 = row ['ID']
            Artist1 = row ['Artist']
            Title1 = row ['Title']
            objFile = open(strFileName, 'a')
            objFile.write(ID1 + '\n')
            objFile.write (Artist1 + '\n')
            objFile.write (Title1 + '\n')
            objFile.close()
        pass
    
    # 6. Exit the program if the user cxhooses so
    elif strChoice == 'x':
        break
    
    else:
        print('Please choose either l, a, i, d, s or x!')

