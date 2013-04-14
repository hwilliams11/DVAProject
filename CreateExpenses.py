from Categorize import getDirectory
from random import *
from copy import deepcopy


months = [31,28,31,30,31,30,31,31,30,31,30,31]
    
class Expense:
    expenseId = 1
    def __init__(self,description,date,category,paid,amount,userid,splitId=-1):
        
        if splitId != -1:
            self.id = splitId
        else:
            self.id = Expense.expenseId
            Expense.expenseId = Expense.expenseId+1
            
        self.description = description
        self.date = date
        self.category = category
        self.paid = paid
        self.amount = amount
        self.userid = userid
        

    @staticmethod
    def splitExpense(store,date,category,cost,userSplit):

        splitId = Expense.expenseId
        splitExpenses = {}
        count = 1
        left = cost
        
        for userid,frac in userSplit.items():
            myCost = round(frac*cost,2)
            if count == len(userSplit):
                if left > myCost or left < myCost:
                    myCost = left
                    
            left = left - myCost
            splitExpenses[userid] = Expense(store,date,category,myCost,cost,userid,splitId)
            count = count + 1

        Expense.expenseId = Expense.expenseId+1
        return splitExpenses
    
    def __str__(self):
        return "User id: "+str(self.userid)+" Expense id:"+str(self.id)+" "+self.description+" "+str(self.amount)

    def __repr__(self):
        return self.__str__()
        

def createExpenses(users,directory):

    expenses = {}
    for user in users:
        userid = users[user]
        expenses[userid]={}
        for year in years:
            expenses[userid][year] = {}
            for month in range(len(months)):
                expenses[userid][year][month]=[]
                
    for user in users:
        generateYearlyExpenses(users,expenses,user,years,directory)

    return expenses
            
def generateYearlyExpenses(users,allExpenses,user,years,directory):
    categories = directory.keys()
    maxVal = {'grocery':3, 'transportation':8, 'entertainment':3, 'shopping':5, 'utilities':2, 'home':4, 'special':1, 'restaurants':10}
    costRange = {'grocery':(20,200),'transportation':(20,100),'entertainment':(5,30),'shopping':(20,200),'utilities':(50,300),'home':(10,500),'special':(100,5000),'restaurants':(5,50)}

    userid = users[user]
    userExpenses = allExpenses[userid]
    
    for year in years:
        for month in range(len(months)):
            for category in maxVal:
                if category == 'special' and random()<.05:
                    numExpenses = 1
                elif category == 'special':
                    numExpenses = 0                        
                else:
                    numExpenses = randint(0,maxVal[category])
                for i in range(numExpenses):

                    
                    storeI = randint( 0,len(directory[category])-1 )
                    store = directory[category][storeI]
                    day = randint(1,months[month])
                    date = (month+1,day,year)
                    cost = randint( costRange[category][0],costRange[category][1] )
                    
                    if cost > 10 and random()< .1 :
                        splitExpense(store,month,day,year,category,cost,allExpenses,user,users)
                    else:
                        expense = Expense(store,date,category,cost,cost,users[user])
                        userExpenses[year][month].append(expense)
                          
                    

    
def equalSplit(userSplit):

    totalUsers = len(userSplit)
    frac = 1.0/totalUsers
    for user in userSplit:
        userSplit[user]=frac
        
def unequalSplit(userSplit):

    totalUsers = len(userSplit)
    equalFrac = 1.0/totalUsers
    left = 1
    percs = [i/100.0 for i in range(60,110,10)]
    count = 1
    
    for user in userSplit:
        
        
        if count == len(userSplit):
            userSplit[user] = left
        else:
            perc = sample(percs,1)[0]
            frac = perc*equalFrac
            userSplit[user] = frac
            
        left = left - frac
        count = count + 1
    
def splitExpense(store,month,day,year,category,cost,expenses,user,users):

    numToSplitWith = randint(1,len(users)-1)
    listUsers = users.items()
    userSplit = {}
    shuffle(listUsers)
    count = 0
    date = (month+1,day,year)
    
    for currUser in listUsers:
        if currUser[0] != user:
            userSplit[currUser[1]]=0
            count = count + 1
        if count == numToSplitWith:
            break

    userSplit[users[user]]=0

    if random() < .7:
        equalSplit(userSplit)
    else:
        unequalSplit(userSplit)

    splitExpenses = Expense.splitExpense(store,date,category,cost,userSplit)
    #print splitExpenses

    for userid in userSplit:
        expenses[userid][year][month].append(splitExpenses[userid])
    
    

    
    
            
def writeFile(expenses,users):
    expensesFile = file('Expenses.csv','w')
    expenseUserFile = file('ExpenseUser.csv','w')
    expensesFile.write("E ID,date,description,amount,category\n")
    expenseUserFile.write("EID,UID,Paid,ExpenseShared\n")

    wroteExpense = {}
    
    for user in users:
        userid = users[user]
        for year in expenses[userid]:
            for month in expenses[userid][year]:
                for expense in expenses[userid][year][month]:
                    date  = expense.date
                    dateStr = str(date[0])+"-"+str(date[1])+"-"+str(date[2])
                    #data1 = str(expense.id)+","+dateStr+",\""+expense.description+"\","+str(expense.amount)+","+expense.category+"\n"
                    data1 = "%d,%s,\"%s\",%.2f,%s\n"%(expense.id,dateStr,expense.description,expense.amount,expense.category)
                    #data2 = str(expense.id)+","+str(userid)+","+str(expense.paid)+","+str(expense.amount)+"\n"
                    data2 = "%d,%d,%.2f,%.2f\n" % (expense.id,userid,expense.paid,expense.amount)
                    if expense.id not in wroteExpense:
                        expensesFile.write(data1)
                    expenseUserFile.write(data2)
                    wroteExpense[expense.id]=True
                    
    expensesFile.close()
    expenseUserFile.close()

users = {'Rahul Agrawal':1,'Yi Ding':2,'Holly Williams':3,'Anqi Zou':4}
years = [2012,2013]

directory = getDirectory()
expenses = createExpenses(users,directory)

writeFile(expenses,users)
