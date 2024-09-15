decks = {}
player_decks = {}

while entry := input():
    name, number = entry.split(' / ')
    if name.isdecimal():
        decks[name] = decks.get(name, set()) | {number}
    else:
        player_decks[name] = player_decks.get(name, set()) | {number}

greatest_game_set = 0
player_set = {}
for player, p_d in player_decks.items():
    cur_deck = set()
    for deck in p_d:
        cur_deck |= decks[deck]
    greatest_game_set = max(greatest_game_set, len(cur_deck))
    player_set[player] = len(cur_deck)

goats = []
for player, cards in player_set.items():
    if cards == greatest_game_set:
        goats.append(player)

print(*sorted(goats), sep='\n')
