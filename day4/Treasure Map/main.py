row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

#horizaontal and vertical
h = int(position[1])
v = int(position[0])

map[h-1][v-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
