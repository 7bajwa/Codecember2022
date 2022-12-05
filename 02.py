f = open('c:/Projects/Python/Codecember/02/02_input.txt', 'r')
a, x = zip(*[x.split(' ') for x in [x.strip() for x in f.readlines()]])


my_choice_value = 0
my_win_value = 0

for i in x:
    if i == "X":
        my_choice_value += 1
    elif i == "Y":
        my_choice_value += 2
    elif i == "Z":
        my_choice_value += 3

for i in range(0,len(a)):
    if x[i]=="X" and a[i] == "A":
        my_win_value += 3
    elif x[i]=="Y" and a[i] == "B":
        my_win_value += 3  
    elif x[i]=="Z" and a[i] == "C":
        my_win_value += 3  
    elif x[i]=="X" and a[i] == "C":
        my_win_value += 6
    elif x[i]=="Y" and a[i] == "A":
        my_win_value += 6
    elif x[i]=="Z" and a[i] == "B":
        my_win_value += 6      

print("My total score is " + str(my_choice_value+my_win_value)) 



choice_value = 0
win_value = 0

for i in range(0,len(x)):
    if x[i]=="X":
        win_value += 0
        if a[i] == "A":
            choice_value += 3
        elif a[i] == "B":
            choice_value += 1
        elif a[i] == "C":
            choice_value += 2
    if x[i]=="Y":
        win_value += 3 
        if a[i] == "A":
            choice_value += 1
        elif a[i] == "B":
            choice_value += 2
        elif a[i] == "C":
            choice_value += 3 
    if x[i]=="Z":
        win_value += 6
        if a[i] == "A":
            choice_value += 2
        elif a[i] == "B":
            choice_value += 3
        elif a[i] == "C":
            choice_value += 1  

print("My cryptic score is " + str(choice_value+win_value)) 
