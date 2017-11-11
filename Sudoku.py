emoty_places = 81
chart=[0 for x in range(81)]
optional_numbers=[[True for x in range(9)]for x in range(81)]

def get_row(row_num):
    start_row =row_num*9
    row_inedxs=[i for i in range(start_row,start_row+9)]
    return row_inedxs

def get_column(column_num):
    column_inedxs=[i for i in range(column_num,81,9)]
    return column_inedxs

def get_dice(dice_num):
    dice_inedxs=[]
    start_dice=(int(dice_num/3)*27)+((dice_num%3)*3)
    for i in range(start_dice,start_dice+20,9):
        for j in range (i,i+3):
            dice_inedxs.append(j)
    return dice_inedxs

def read_from_file():
    file = open("input.txt", "r")
    for line in file:
        row, column, num = map(int, line.split(":"))
        index=((row-1)*9)+(column-1)
        insert_num(index,num)
def print_chart(arr):
    for i in range(0,81,9):
        for j in range(i,i+9):
            print(repr(arr[j]).rjust(2),end=' ')
        print()

def place_by_index(index):
    column =  index % 9
    row=int(index/9)
    dice=(int(index/27)*3)+int((index%9)/3)
    return [row,column,dice]

def chack_if_legal(index,num):
    row,column,dice = place_by_index(index)
    for i in get_row(row):
       if chart[i] == num:
           return False

    for i in get_column(column):
        if chart[i] == num:
            return False

    for i in get_dice(dice):
        if chart[i] == num:
            return False
    return True

def finish_gime():
    print_chart(chart)
    exit()

def insert_num(index,num):
    global emoty_places
    if(chack_if_legal(index, num)== False):
         print("you heva problem")
         exit(1)
    chart[index]=num
    emoty_places -= 1
    if (emoty_places == 0):
        finish_gime()
    row, column, dice = place_by_index(index)
    for i in get_row(row):
        optional_numbers[i][num-1] = False
    for i in get_column(column):
        optional_numbers[i][num - 1] = False
    for i in get_dice(dice):
       optional_numbers[i][num - 1] = False
    for i in range(9):
        optional_numbers[index][i] = False

def find_number(index):
    for num in range(9):
        if optional_numbers[index][num] and committed_num(index,num):
            insert_num(index,num+1)
def committed_num (index,num):
    row, column, dice = place_by_index(index)
    return chack_row(index,row,num) or chack_dice(index,dice,num) or chack_column(index,column,num)
def chack_row(index,row,num):
    for i in get_row(row):
        if  i == index:
            continue
        if optional_numbers[i][num]== True:
            return False
    return True
def chack_column(index,columan,num):
    for i in get_column(columan):
        if  i == index:
            continue
        if optional_numbers[i][num]== True:
            return False
    return True
def chack_dice(index,dice,num):
    for i in get_dice(dice):
        if  i == index:
            continue
        if optional_numbers[i][num]== True:
            return False
    return True

read_from_file()
for j in range(81):
     for i in range(81):
         find_number(i)
print_chart(chart)