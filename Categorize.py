'''
Created on Apr 5, 2013

@author: Holly
'''

def stringDiff( expense, directoryItem ):
    import difflib
    expenseTokens = expense.lower().split()
    dirItemTokens = directoryItem.lower().split()
    matchedTokens = len([item for item in expenseTokens if item in dirItemTokens])
    ratio = difflib.SequenceMatcher(None,expense,directoryItem).ratio()
    if ratio > .5:
        return ratio
    else:
        return 0
    

def matchTokens( expense, directoryItem ):
    expenseTokens = expense.lower().split()
    dirItemTokens = directoryItem.lower().split()
    matchedTokens = len([item for item in expenseTokens if item in dirItemTokens])
    return matchedTokens
    
def getScore(expense,categoryList,match=matchTokens):
    count = 0
    for item in categoryList:
        count = count + match(expense,item)
    return count

def categorizeExpense(expense,directory,match=matchTokens):
    scores = {}
    for category in directory.keys():
        score = getScore( expense, directory[category], match )
        scores[category] = score
    max = -1
    nonzero = 0
    
    for value in scores.values():
        if value!=0:
            nonzero = True
            break

    if not nonzero:
        return 'misc'
    
    for category in scores.keys():
        if max == -1:
            max = category
        elif scores[max]< scores[category]:
            max = category
    return max

def categorizeExpenses(expenses,directory,match=matchTokens):
    categories = {}
    for expense in expenses:
        categories[expense] = categorizeExpense(expense,directory,match) 
    return categories

def getDirectory():

    folder = "Directory Data\\"
    filenames = {
                 'entertainment':'Entertainment.txt',
                 'grocery':'Grocery-Stores.txt',
                 'home':'Home.txt',
                 'restaurants':'Restaurants.txt',
                 'shopping':'Shopping.txt',
                 'special':'Special.txt',
                 'transportation':'Transportation.txt',
                 'utilities':'Utilities.txt',
                 }
    
    directory = {}
    for category in filenames.keys():
        filename = folder+filenames[category]
        directory[category] = [line.strip() for line in file(filename)]
    return directory

expenses01 = ['Publix',
              'Cypress St',
              'Post Property',
              "Mary Mac's",
              'Publix',
              'Tin Drum',
              'Chevron',
              'CVS',
              'Amazon',
              'Ri Ra Irish',
              'Marta',
              'CVS',
              'American Haircut',
              'LinkedIn',
              'Ga Tech CRC',
              'Amazon',
              'Gilt Groupe',
              'Publix',
              'Starbucks',
              'The Ivy Buckhead',
              'The Ivy Buckhead',
              'The Ivy Buckhead',
              'Office Depot',
              'Costco',
              'QuickTrip']

expenses26 = ['Rave movies',
            'Subway food',
            'Dish Network cable',
            'Belk shopping',
            'Ikea furniture',
            'BP gas',
            'Georgia Southern tuition',
            'Burger King',
            'Walmart dvd',
            'Moes food',
            'AT&T internet',
            'Sprint phone',
            'Target furniture',
            'Shell gas',
            'West Mar rent',
            'AT&T cell phone',
            'Netflix monthly',
            'Applebees food',
            'Comcast phone',
            'Target school supplies',
            'Target cleaning supplies',
            'Delta plane ticket',
            'H&M clothes',
            'Barnes and Noble book',
            'Georgia Power water/gas/sewer']

expenses76 = ['Walmart Howell Mill Rd',
              'Target Atlantatic Station',
              'Walmart.com',
              'Publix Midtown',
              'Kroger Howell Mill Rd',
              "Wendy's Howell Mill Rd",
              "McDonald's Northside Dr",
              'Georgia Power',
              'At&t.com',
              'Regal Atlantic Station',
              'Marta', 'Emory Hospital',
              'Home Depot Buckhead',
              "Lowe's East Point",
              'Hartsfield-Jackson Airport',
              'Bestbuy.com',
              'Newegg.com',
              '6pm.com',
              'Delta.com',
              'Chow Baby Howell Mill Rd',
              'Chick Fil A Georgia Tech',
              'Amazon.com',
              'Great Wall Supermarket',
              "Ming's BBQ",
              'UPS store']

directory = getDirectory()

for expense in expenses01:
    category = categorizeExpense(expense,directory,stringDiff)
    print expense+" : "+category
