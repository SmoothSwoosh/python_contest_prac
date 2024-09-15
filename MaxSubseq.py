max_seq, seq = 0, 0
prev_num = None
while num:=int(input()):
    if prev_num is None:
        seq = 1
    elif prev_num <= num:
        seq += 1
    else:
        max_seq = max(max_seq, seq)
        seq = 1
    prev_num = num

max_seq = max(max_seq, seq)
print(max_seq)
