import sys

def get_part_1(player_1, player_2):
    ans = 0

    if len(player_1) != 0:
        player = player_1
    else:
        player = player_2

    player.reverse()
    for i in range(len(player)):
        ans += (i+1) * player[i]

    return ans

def solution(filename):
    f = open("./inputs/" + filename, 'r')
    f = f.read().split("\n\n")  # f[0].split("\n")[1:] is player1, f[1][1:] is player 2

    player_1 = []
    player_2 = []

    for num in f[0].split("\n")[1:]:
        print('>>>{}<<<<'.format(num))
	if num != '':
            player_1.append(int(num))

    for n in f[1].split("\n")[1:]:
	if n != '':
            player_2.append(int(n))

    while len(player_2) != 0 and len(player_1) != 0:
        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)

        if card_1 > card_2:
            player_1.append(card_1)
            player_1.append(card_2)

        else:   # card_2 > card_1
            player_2.append(card_2)
            player_2.append(card_1)

    return get_part_1(player_1, player_2)



f_name = sys.argv[1]
print(solution(f_name))

