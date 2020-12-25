import sys

def get_score(player):
    ans = 0

    player.reverse()
    for i in range(len(player)):
        ans += (i+1) * player[i]

    return ans

def compare_cards(card_1, card_2):
    if card_1 > card_2:
        return 1
    return 2

def get_winner(player_1, player_2):
    old_orientations = []

    while len(player_1) != 0 and len(player_2) != 0:

        if [player_1, player_2] in old_orientations:
            return 1, player_1

        old_orientations.append([player_1.copy(), player_2.copy()])

        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)

        if card_1 <= len(player_1) and card_2 <= len(player_2):
            who_won_round, filler = get_winner(player_1[:card_1], player_2[:card_2])
        else:
            who_won_round = compare_cards(card_1, card_2)

        if who_won_round == 1:
            player_1.append(card_1)
            player_1.append(card_2)
        if who_won_round == 2:
            player_2.append(card_2)
            player_2.append(card_1)


    if len(player_1) == 0:
        return 2, player_2
    else:
        return 1, player_1


def solution(filename):
    f = open("./inputs/" + filename, 'r')
    f = f.read().split("\n\n")  # f[0].split("\n")[1:] is player1, f[1][1:] is player 2

    player_1 = []
    player_2 = []

    for num in f[0].split("\n")[1:]:
        player_1.append(int(num))

    for num in f[1].split("\n")[1:]:
        player_2.append(int(num))

    who_won, winning_cards = get_winner(player_1, player_2)

    return get_score(winning_cards)



f_name = sys.argv[1]
print(solution(f_name))

