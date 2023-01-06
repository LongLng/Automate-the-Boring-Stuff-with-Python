#Fantasy Game Inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v , k),
        item_total = item_total + int(v)
    print("Total number of items: " + str(item_total))
    
#List to Dictionary Function for Fantasy Game Inventory
def addToInventory(inventory,addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            inventory[addedItems[i]] +=1
        else:
            inventory.setdefault(addedItems[i],1)
    return inventory
        
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

if __name__ == '__main__':
	inv = {'gold coin': 42, 'rope': 1}
	inven = addToInventory(inv, dragonLoot)
	displayInventory(inven)