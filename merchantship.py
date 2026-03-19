Merchant_Ship_Items = [

    {
        "name": "Sword",
        "price": 10,
        "Weapon Type": "Medium",
        "description": "A blade of fine craft, likely an heirloom of whoever held the blade before it was pilfered from their remains."
    },
    {
        "name": "Battleaxe",
        "price": 10,
        "Weapon Type": "Heavy",
        "description": "A sturdy axe perfect for splitting bone."
    },
    {
        "name": "Stiletto",
        "price": 10,
        "Weapon Type": "Light",
        "description": "A remarkably thin blade often likened to (and used as) a toothpick."
    },
    {
        "name": "Iron Spear",
        "price": 12,
        "Weapon Type": "Medium",
        "description": "A spear perfect for poking at a safe distance."
    },
    {
        "name": "Mace",
        "price": 15,
        "Weapon Type": "Medium",
        "description": "A simple blunt weapon effective at breaking guards."
    },
    {  
        "name": "Flintlock",
        "price": 50,
        "Weapon Type": "Light",
        "description": "The son of a village blacksmith, a young Gunsmith Rosen took to the seas and returned an older man, bringing with him the spark of inspiration that brought firearms into the world. The modern flintlock is an improved and lightweight version of Gunsmith's prototype now found in every Luminant."
    },
    {
        "name": "Apprentice Rapier",
        "price": 12,
        "Weapon Type": "Light",
        "description": "Although fragile in appearance, this beginner's blade has been the starting point for many Pathfinders beginning their journey."
    },
    {
        "name": "Zweihander",
        "price": 20,
        "Weapon Type": "Heavy",
        "description": "Popularised by the Canor Borderwatchers, the Zweihander is as fearsome as it is heavy."
    },
    {
        "name": "Iron Cestus",
        "price": 15,
        "Weapon Type": "Light",
        "description": "Your own two fists. Worth a shot, right?"
    },
    {
        "name": "Steel Maul",
        "price": 20,
        "Weapon Type": "Heavy",
        "description": "A sturdy maul perfect for knocking walls and people down alike."
    }
]

cart = []
shopping = True
number = 0
prices = 0
for index, item in enumerate(Merchant_Ship_Items):
    print(index, ":", item["name"])

while shopping == True:
    choice = int(input ("What would you like to buy, Pathfinder?"))
    cart.append((Merchant_Ship_Items[choice]))
    print ("Would you like to continue shopping?")
    print ("1: Yes")
    print ("2: No")
    number = int((input("Answer:")))
    if number == 1:
        shopping = True
    elif number == 2:
        break

for i in cart:
    prices = prices+i["price"]

print (cart ["name"])
print ("Amount due:", prices)




# print (Merchant_Ship_Items[choice]["name"])