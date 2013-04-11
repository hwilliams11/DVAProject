"""
Author: Rahul

Simpe script that works over split.txt to construct expense and expenseuser tables

"""

import datetime

with open('split.txt', 'r') as f:
    data = f.readlines()

fexp = open("expensetab.txt", 'w')
fexpusr = open("expense_usertab.txt", 'w')
data = [i.strip().split(';') for i in data]
nd = [[i[0], i[1], float(i[3])] + map(float,i[5:]) for i in data[1:]]
for i in nd:
    i[0] = datetime.date(*map(int, i[0].split('-')))

def per2exp_filter(exp):
    return exp[-1] == 0 or exp[-2] == 0 or exp[-3] == 0

per2exp = filter(per2exp_filter, nd)


def splitexp_filter(exp):
    return (exp[-1] == 0 or abs(exp[-1]) == exp[2]) and (exp[-2] == 0 or abs(exp[-2]) == exp[2]) and (exp[-3] == 0 or abs(exp[-3]) == exp[2])


per2exp_split = filter(lambda x: not(splitexp_filter(x)), per2exp)
    
for num, exp in enumerate(per2exp_split):
    exp_sum = sum(map(abs, exp[-3:]))
    fexp.write("\t".join(map(str,[num, exp[1], exp_sum, None, exp[0]]))+"\n")
    if exp[-1] < 0:
        fexpusr.write("\t".join(map(str, [num, 1, 0, abs(exp[-1])]))+"\n")
    elif exp[-1] > 0:
        fexpusr.write("\t".join(map(str, [num, 1, exp_sum, exp[-1]]))+"\n")
    if exp[-2] < 0:
        fexpusr.write("\t".join(map(str, [num, 2, 0, abs(exp[-2])]))+"\n")
    elif exp[-2] > 0:
        fexpusr.write("\t".join(map(str, [num, 2, exp_sum, exp[-2]]))+"\n")
    if exp[-3] < 0:
        fexpusr.write("\t".join(map(str, [num, 3, 0, abs(exp[-3])]))+"\n")
    elif exp[-3] > 0:
        fexpusr.write("\t".join(map(str, [num, 3, exp_sum, exp[-3]]))+"\n")

per2exp_direct = filter(splitexp_filter, per2exp)
for num, exp in enumerate(per2exp_direct):
    num = num + len(per2exp_split)
    fexp.write("\t".join(map(str,[num, exp[1], exp[2], None, exp[0]]))+"\n")
    if exp[-1] < 0:
        fexpusr.write("\t".join(map(str, [num, 1, 0, abs(exp[-1])]))+"\n")
    elif exp[-1] > 0:
        fexpusr.write("\t".join(map(str, [num, 1, exp[-1], 0]))+"\n")
    if exp[-2] < 0:
        fexpusr.write("\t".join(map(str, [num, 2, 0, abs(exp[-2])]))+"\n")
    elif exp[-2] > 0:
        fexpusr.write("\t".join(map(str, [num, 2, exp[-2], 0]))+"\n")
    if exp[-3] < 0:
        fexpusr.write("\t".join(map(str, [num, 3, 0, abs(exp[-3])]))+"\n")
    elif exp[-3] > 0:
        fexpusr.write("\t".join(map(str, [num, 3, exp[-3], 0]))+"\n")

per3exp = filter(lambda x: not(per2exp_filter(x)), nd)
for num, exp in enumerate(per3exp):
    num = num + len(per2exp)
    fexp.write("\t".join(map(str,[num, exp[1], exp[2], None, exp[0]]))+"\n")
    if exp[-1] < 0:
        fexpusr.write("\t".join(map(str, [num, 1, 0, abs(exp[-1])]))+"\n")
    elif exp[-1] > 0:
        fexpusr.write("\t".join(map(str, [num, 1, exp[2], exp[2]-exp[-1]]))+"\n")
    if exp[-2] < 0:
        fexpusr.write("\t".join(map(str, [num, 2, 0, abs(exp[-2])]))+"\n")
    elif exp[-2] > 0:
        fexpusr.write("\t".join(map(str, [num, 2, exp[2], exp[2]-exp[-2]]))+"\n")
    if exp[-3] < 0:
        fexpusr.write("\t".join(map(str, [num, 3, 0, abs(exp[-3])]))+"\n")
    elif exp[-3] > 0:
        fexpusr.write("\t".join(map(str, [num, 3, exp[2], exp[2]-exp[-3]]))+"\n")
        
fexp.close()
fexpusr.close()