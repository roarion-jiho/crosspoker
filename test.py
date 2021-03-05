import random, judge
#from collections import Counter

# make a list of whole cards
def card_list():
    numbers = [8, 9, 10, 11, 12, 13, 14]
    shapes = [1, 2, 3, 4]
    #shapes = ['\u2665','\u2663','\u2660','\u2666']
    cards = list()
    for i in shapes:
        for j in numbers:
            match = [j,i]
            cards.append(match)
    return cards

# color
def color_match(card):
    color_list = list()
    for i in range(0,5):
        if card[i][1] == 1 or card[i][1] == 4:
            color_list.append("red")
        else:
            color_list.append("black")
    return color_list

# arrange 5 by 5
def arrange_card():
    cards = list()
    for i in range(0,25):
        cards.append([100,200])
    # arrange to 5 by 5 form
    arranged_cards = list()
    for i in range(0,5):
        arranged_cards.append([cards[i*5], cards[i*5 + 1], cards[i*5 + 2], cards[i*5 + 3], cards[i*5 + 4]])
    # ============= choose flush shape =============
    flu_shps = []  # flush shapse
    shapes = random.randint(1, 4)
    for i in range(0, 3):
        while shapes in flu_shps:
            shapes = random.randint(1, 4)
        flu_shps.append(shapes)
    # make Straights: 1) first straight =============
    straight1 = []
    straight1.append(random.randint(8, 10))
    for i in range(1, 5):
        straight1.append(straight1[0] + i)
    random.shuffle(straight1)
    # ============= make Straights: 1) first straight
    # make Straights: 2) second straight =============
    straight2 = []
    straight2.append(random.randint(8, 10))
    for i in range(1, 5):
        straight2.append(straight2[0] + i)
    random.shuffle(straight2)
    check = 0
    while check == 0:
        random.shuffle(straight2)
        check = (straight1[0] - straight2[0]) * (straight1[1] - straight2[1]) * (straight1[2] - straight2[2]) * (straight1[3] - straight2[3]) * (straight1[4] - straight2[4])
    # ============= make Straights: 2) second straight
    flu_rows = [] # flush rows
    str_cols = [] # straight cols
    # choose 3 rows to make flushes
    row_num = random.randint(0,4)
    for i in range(0,3):
        while row_num in flu_rows:
            row_num = random.randint(0,4)
        flu_rows.append(row_num)
    flu_rows.sort()
    # choose 2 cols to make straights
    col_num = random.randint(0,4)
    for i in range(0,2):
        while col_num in str_cols:
            col_num = random.randint(0,4)
        str_cols.append(col_num)
    str_cols.sort()
    # match shapes to each flush rows
    for i in range(0,3):
        for j in range(0,5):
            arranged_cards[flu_rows[i]][j][1] = flu_shps[i]
    # match numbers to each straight cols
    for i in range(0,5):
        arranged_cards[i][str_cols[0]][0] = straight1[i]
        arranged_cards[i][str_cols[1]][0] = straight2[i]
    # complete shapes of straight lines ============
    etc_rows = list(set([0, 1, 2, 3, 4]) - set(flu_rows))
    etc_cols = list(set([0, 1, 2, 3, 4]) - set(str_cols))
    for i in range(0, 2):
        for j in range(0, 2):
            check = [400, 500]
            check[0] = arranged_cards[etc_rows[i]][str_cols[j]][0]
            check[1] = random.randint(1, 4)
            check_list = arranged_cards[0] + arranged_cards[1] + arranged_cards[2] + arranged_cards[3] + arranged_cards[4]
            while check in check_list:
                check[1] = random.randint(1, 4)
            arranged_cards[etc_rows[i]][str_cols[j]][1] = check[1]
    a = random.choice([1,2,3,4])
    check_list = arranged_cards[0] + arranged_cards[1] + arranged_cards[2] + arranged_cards[3] + arranged_cards[4]
    ### 1, 2
    a = []
    for i in range(0,2):
        a.append(random.choice([1, 2, 3, 4]))
        while [arranged_cards[etc_rows[0]][str_cols[i]][0], a[i]] in check_list:
            a[i] = random.choice([1, 2, 3, 4])
        arranged_cards[etc_rows[0]][str_cols[i]][1] = a[i]
        check_list.append([arranged_cards[etc_rows[0]][str_cols[i]][0], a[i]])
    ### 3
    b = [1, 2, 3, 4]
    if a[0] == a[1]:
        b.remove(a[0])
    a.append(random.choice(b))
    while [arranged_cards[etc_rows[1]][str_cols[0]][0], a[2]] in check_list:
        a[2] = random.choice(b)
    arranged_cards[etc_rows[1]][str_cols[0]][1] = a[2]
    check_list.append([arranged_cards[etc_rows[1]][str_cols[0]][0], a[2]])
    ### 4
    b = [1, 2, 3, 4]
    if (a[0] == a[1]) or (a[0] == a[2]):
        b.remove(a[0])
    elif a[1] == a[2]:
        b.remove(a[1])
    a.append(random.choice(b))
    while [arranged_cards[etc_rows[1]][str_cols[1]][0], a[3]] in check_list:
        a[3] = random.choice(b)
    arranged_cards[etc_rows[1]][str_cols[1]][1] = a[3]
    # ============ complete shapes of straight lines
    # complete numbers in flushe lines ============
    nums_flu1_etc = list(
        set([8, 9, 10, 11, 12, 13, 14]) - set([straight1[flu_rows[0]]]) - set([straight2[flu_rows[0]]]))
    nums_flu2_etc = list(
        set([8, 9, 10, 11, 12, 13, 14]) - set([straight1[flu_rows[1]]]) - set([straight2[flu_rows[1]]]))
    nums_flu3_etc = list(
        set([8, 9, 10, 11, 12, 13, 14]) - set([straight1[flu_rows[2]]]) - set([straight2[flu_rows[2]]]))
    flu1_etc_cards = []
    flu2_etc_cards = []
    flu3_etc_cards = []
    check_list = arranged_cards[0] + arranged_cards[1] + arranged_cards[2] + arranged_cards[3] + arranged_cards[4]
    for i in nums_flu1_etc:
        while [i, flu_shps[0]] not in check_list:
            flu1_etc_cards.append([i, flu_shps[0]])
            check_list.append([i, flu_shps[0]])
    for i in nums_flu2_etc:
        while [i, flu_shps[1]] not in check_list:
            flu2_etc_cards.append([i, flu_shps[1]])
            check_list.append([i, flu_shps[1]])
    for i in nums_flu3_etc:
        while [i, flu_shps[2]] not in check_list:
            flu3_etc_cards.append([i, flu_shps[2]])
            check_list.append([i, flu_shps[2]])
    random.shuffle(flu1_etc_cards)
    random.shuffle(flu2_etc_cards)
    random.shuffle(flu3_etc_cards)
    for i in range(0, 3):
        arranged_cards[flu_rows[0]][etc_cols[i]] = flu1_etc_cards[i]
        arranged_cards[flu_rows[1]][etc_cols[i]] = flu2_etc_cards[i]
        arranged_cards[flu_rows[2]][etc_cols[i]] = flu3_etc_cards[i]
    # ============ complete numbers in flushe lines
    # input other cards
    all_cards = card_list()
    for i in range(0, 5):
        for j in range(0, 5):
            if arranged_cards[i][j] in all_cards:
                all_cards.remove(arranged_cards[i][j])
    random.shuffle(all_cards)
    for i in range(0, 5):
        for j in range(0, 5):
            if arranged_cards[i][j] == [100, 200]:
                arranged_cards[i][j] = all_cards.pop(0)
    # Decide: Are flushes in rows or cols?
    row_or_col = random.randint(0, 1)  # 0 = rows, 1 = cols
    if row_or_col == 1:
        new_arrange = []
        for i in range(0, 5):
            new_arrange.append(
                [cards[i * 5], cards[i * 5 + 1], cards[i * 5 + 2], cards[i * 5 + 3], cards[i * 5 + 4]])
        for i in range(0, 5):
            for j in range(0, 5):
                new_arrange[i][j] = arranged_cards[j][i]
        arranged_cards = new_arrange
    # match colors after arrangement
    colors = [1, 2, 3, 4, 5]
    for i in range(0, 5):
        colors[i] = color_match(arranged_cards[i])
    return arranged_cards[0], arranged_cards[1], arranged_cards[2], arranged_cards[3], arranged_cards[4], colors[0], colors[1], colors[2], colors[3], colors[4], flu_rows, str_cols, etc_cols

test = arrange_card()
print(test[0])
print(test[1])
print(test[2])
print(test[3])
print(test[4])
print(test[10])
print(test[11])
print(test[12])