'''
Part 1: Find the highest seat ID on a boarding pass
seat = 8 letter string (first 5 = row, last 3 = column)
Using binary search to find the seat row and column
seat ID = row * 8 + column

Part 2: Find the seat that is missing
missing seat = All possible seats in range - all that exist
'''
inputfile = open('inputDay05.txt','r')
seats = [i.rstrip('\n') for i in inputfile.readlines()]

def search_seat(seat):
    row_seat = [i for i in seat if i in "FB"]
    column_seat = [i for i in seat if i in "RL"]
    range_row = list(range(128))
    range_column = list(range(8))

    for letter in row_seat:
        mid = int(len(range_row)/2)
        if letter == "F":
            range_row = range_row[:mid]
        else:
            range_row = range_row[mid:]
    row = range_row[0]

    for letter in column_seat:
        mid = int(len(range_column)/2)
        if letter == "L":
            range_column = range_column[:mid]
        else:
            range_column = range_column[mid:]
    column = range_column[0]

    return row,column

def seat_ID(row,column):
    return row*8+column

def scan_all_seats(seats):
    allseats = []
    all_seat_ids = []
    for i in seats:
        seat = search_seat(i)
        allseats.append(seat)
        all_seat_ids.append(seat_ID(seat[0],seat[1]))
    my_seat = list(set(range(min(all_seat_ids),max(all_seat_ids)+1)) - set(all_seat_ids))[0]
    return max(all_seat_ids), my_seat

part1,part2 = scan_all_seats(seats)

print("Part 1:",part1)
print("Part 2:",part2)

inputfile.close()