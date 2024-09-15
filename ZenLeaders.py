def get_stats(record):
    name, surname, *team, time = record
    return list([name, surname, ' '.join(team), time])


def read_and_process():
    table = []
    while record := input().split():
        table.append(get_stats(record))
        
    return table


def comp(member):
    #firstly sort by time, then if times are equal, by surname, then name and team
    return (list(map(int, member[-1].split(':'))), member[1], \
            member[0], member[2])


def get_winners(table):
    if not table:
        return []
    
    num_of_winners = 3
    unique_times = set()
    
    for i, member in enumerate(table):
        if member[-1] not in unique_times:
            unique_times.add(member[-1])
        if len(unique_times) > num_of_winners:
            return table[:i]
    else:
        return table[:i + 1]


def print_table(winners):
    if not winners:
        return
    
    length = [0] * 4
    
    for i in range(len(length)):
        length[i] = len(max(winners, key = lambda item: len(item[i]))[i])

    fmt = "{{:<{0}}} {{:<{1}}} {{:<{2}}} {{:<{3}}}".format(*length)
    for member in winners:
        print(fmt.format(*member))


table = read_and_process()
table.sort(key = comp)
winners = get_winners(table)
print_table(winners)
