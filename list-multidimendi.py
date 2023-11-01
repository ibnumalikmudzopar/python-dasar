list_minuman = [
    ["Kopi", "Teh", "Marimas"],
    ["Adem Sari", "Ale-Ale", "Pocari"],
    ["TeaJus", "Sprite", "Fanta"]
]

print(list_minuman[2][0])
print("-" * 10)
for menu in list_minuman:
    for minuman in menu:
        print(minuman)
