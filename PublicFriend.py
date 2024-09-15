friends = {}

while pair := eval(input()):
    m, n = pair
    if m == 0 and n == 0:
        break
    friends[m] = friends.get(m, set()) | {n}
    friends[n] = friends.get(n, set()) | {m}

public_friends = []
num_of_friends = len(friends)
for key, value in friends.items():
    if (len(value) == num_of_friends - 1):
        public_friends.append(key)

print(*sorted(public_friends))
