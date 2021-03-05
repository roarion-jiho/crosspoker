def judge_cards(five_cards):
    if judge_4cards(five_cards) == "4 of a kind":
        result = "4 of a kind"
    elif judge_flush(five_cards) == "Flush":
        if judge_straight(five_cards) == "Straight":
            check = 0
            for i in range(0,5):
                check += five_cards[i][0]
            if check == 60:
                result = "Royal flush"
            else:
                result = "Straight flush"
        else:
            result = "Flush"
    elif judge_fullhouse(five_cards) == "Full house":
        result = "Full house"
    elif judge_straight(five_cards) == "Straight":
        result = "Straight"
    elif judge_pair(five_cards) == "Nothing":
        result = judge_top(five_cards)
    else:
        result = judge_pair(five_cards)
    return result

#sort start
def sel_sort(a):
    n = len(a)
    for i in range(0,n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

#4 of a kind
def judge_4cards(five_cards):
    compared_list = list()
    for i in range(0, 5):  # change type into int
        compared_list.append(int(five_cards[i][0]))
    sorted_cards = sel_sort(compared_list)
    if sorted_cards[0] == sorted_cards[3] or sorted_cards[1] == sorted_cards[4]:
        result = "4 of a kind"
    else:
        result = "Nothing"
    return result

#Flush
def judge_flush(five_cards):
    compared_list = list()
    for i in range(0, 5):  # change type into int
        compared_list.append(int(five_cards[i][1]))
    sorted_cards = sel_sort(compared_list)
    if sorted_cards[0] == sorted_cards[4]:
        result = "Flush"
    else:
        result = "Nothing"
    return result

#Full house
def judge_fullhouse(five_cards):
    compared_list = list()
    for i in range(0, 5):  # change type into int
        compared_list.append(int(five_cards[i][0]))
    sorted_cards = sel_sort(compared_list)
    if (sorted_cards[0] == sorted_cards[2] and sorted_cards[3] == sorted_cards[4]) or (sorted_cards[0] == sorted_cards[1] and sorted_cards[2] == sorted_cards[4]):
        result = "Full house"
    else:
        result = "Nothing"
    return result


#Straight
def judge_straight(five_cards):
    compared_list = list()
    test_list = list()
    for i in range(0,5): #change type into int
        compared_list.append(int(five_cards[i][0]))
    sorted_cards = sel_sort(compared_list)
    test_list.append(sorted_cards[0])
    for i in range(0,4):
        test_list.append(test_list[i]+1)
    if test_list == sorted_cards:
        result = "Straight"
    else:
        result = "Nothing"
    return result

#3 of a kind or pair(s)
def judge_pair(five_cards):
    hands = list()
    # judge a pair
    for i in range(0,4):
        for j in range(i+1,5):
            if five_cards[i][0] == five_cards[j][0]:
                hands.append("pair")
    if len(hands) == 1:
        result = "Pair"
    elif len(hands) == 2:
        result = "2 pairs"
    elif len(hands) == 3:
        result = "3 of a kind"
    else:
        result = "Nothing"
    return result

#top
def judge_top(five_cards):
    compared_list = list()
    for i in range(0, 5):  # change type into int
        compared_list.append(int(five_cards[i][0]))
    result = str(number_to_shape(max(sel_sort(compared_list)))) + " top"
    return result

def number_to_shape(number):
    if number == 11:
        number = "J"
    elif number == 12:
        number = "Q"
    elif number == 13:
        number = "K"
    elif number == 14:
        number = "A"
    return number


"""
list1 = [[1,0],[2,0],[2,0],[4,0],[5,0]]
list2 = [[9,0],[10,0],[11,0],[12,0],[13,0]]
print(judge_straight(list1))
print(judge_straight(list2))
print(judge_pair(list1))
print(judge_pair(list2))
print(judge_cards(list1))
print(judge_cards(list2))
"""