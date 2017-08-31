import os


def length_of_longest_key(inventory):
    longest = "a"
    inv = inventory.keys()
    for it in inv:
        if len(it) > len(longest):
            longest = it
    return len(longest)


def length_of_longest(inventory, counter):
    longest = "a"
    for it in inventory:
        if len(it) > len(longest):
            longest = it
    return len(longest)


def inventory(data):
    os.system('cls' if os.name == 'nt' else 'clear')
    inv = data["inventory"]
    l = length_of_longest_key(inv)
    w = length_of_longest(inv, 3)
    it = length_of_longest(inv, 2)
    bar = (100 * "-")
    print("Inventory:\n"+"Item Name".rjust(l, " ") + "Count".rjust(10, " ") + "Weight".rjust(w + 4, " ") 
          + "Item Type".rjust(it + 4, " "), "\n"+bar)
    for i in inv:
        if inv[i][0] == 0:
            continue
        else:
            item = str(i)
            count = str(inv[i][1])
            weight = str(inv[i][3])
            item_type = str(inv[i][2])
            print("{} {} {} {}".format(item.rjust(l, " "), count.rjust(9, " "), weight.rjust(w + 3, " "), item_type.rjust(it + 3, " ")))

