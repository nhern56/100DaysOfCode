row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = position[0]
vertical = position[1]

if horizontal == "1":
    if vertical == "1":
        row1 = ["X","⬜️️","⬜️️"]
    elif vertical == "2":
        row2 = ["X","⬜️️","⬜️️"]
    else:
        row3 = ["X","⬜️️","⬜️️"]

elif horizontal == "2":
    if vertical == "1":
        row1 = ["⬜️","X","⬜️️"]
    elif vertical == "2":
        row2 = ["⬜️","X","⬜️️"]
    else:
        row3 = ["⬜️","X","⬜️️"]

else:
    if vertical == "1":
        row1 = ["⬜️","⬜️️","X"]
    elif vertical == "2":
        row2 = ["⬜️","⬜️️","X"]
    else:
        row3 = ["⬜️","⬜️️","X"]

print(f"{row1}\n{row2}\n{row3}")
