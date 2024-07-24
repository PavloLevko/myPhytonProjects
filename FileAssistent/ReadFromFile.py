def create_cast_list(filename):
    cast_list = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.split(',')

            cast_list.append(line[0])

    return cast_list

    return cast_list


cast_list = create_cast_list('actor_list.txt')
for actor in cast_list:
    print(actor)
