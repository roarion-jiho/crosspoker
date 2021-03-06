import cardlist, judge, random, copy

def card_info():
    cards = cardlist.arrange_card()
    result_row = list()
    result_column = list()
    result_diagonal = list()
    column_cards = list()
    column_elements = list()
    diagonal_tlbr_cards = list()
    diagonal_trbl_cards = list()
    # judge row
    for i in range(0,5):
        result_row.append(judge.judge_cards(cards[i]))
    # judge colume
    for i in range(0, 5):
        for j in range(0, 5):
            column_elements.append(cards[j][i])
        column_cards.append(column_elements)
        column_elements = []
    for i in range(0,5):
        result_column.append(judge.judge_cards(column_cards[i]))
    # judge diagonal (top-left to bottom-right)
    for i in range(0,5):
        diagonal_tlbr_cards.append(cards[i][i])
    result_diagonal.append(judge.judge_cards(diagonal_tlbr_cards))
    # judge diagonal (top-right to bottom-left)
    a = [4, 3, 2, 1, 0]
    b = [0, 1, 2, 3, 4]
    for i in range(0, 5):
        first = a[i]
        second = b[i]
        diagonal_trbl_cards.append(cards[first][second])
    result_diagonal.append(judge.judge_cards(diagonal_trbl_cards))
    cards_num = cardlist.number_to_shape(cards)
    answer = [cards_num,result_row,result_column,result_diagonal]
    return answer

def hide_cards(cardlist):
    hidden_list = copy.deepcopy(cardlist)
    hidden_card_num = []
    hidden_card_shape = []
    while len(hidden_card_num) < 15:
        card = random.randint(0, 24)
        if card not in hidden_card_num:
            hidden_card_num.append(card)
    while len(hidden_card_shape) < 14:
        card = random.randint(0, 24)
        if card not in hidden_card_shape:
            hidden_card_shape.append(card)
    for i in hidden_card_num:
        n = i // 5
        l = i - (n * 5)
        hidden_list[0][n][l][0] = " "
    for i in hidden_card_shape:
        n = i // 5
        l = i - (n * 5)
        hidden_list[0][n][l][1] = " "
    # first should be 0, second = line, third = order, forth = num or shape
    # list[0][0][0][0] = " "
    return hidden_list

"""
0 -> 0
1 -> 1
2 -> 2
3 -> 3
4 -> 4
5 -> 0
"""