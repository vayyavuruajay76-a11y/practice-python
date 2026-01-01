"""Functions to keep track and alter inventory."""
import copy

def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    s={}
    for i in items:
        if i in s:
            s[i]+=1
        else:
            s[i]=1

    return s

    


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    items_dict=create_inventory(items)
    
    for key,value in items_dict.items():
        if key in inventory.keys():
            inventory[key]=inventory[key]+value
        else:
            inventory.setdefault(key,value)
    return inventory
    
    

    


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    itemlist=create_inventory(items)
    allkeys=inventory.keys()
    for index,value in enumerate(items):
        if value in allkeys and inventory[value]>0:
            inventory[value]-=1


    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory.keys():
        inventory.pop(item)
    return inventory

    


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    ls=copy.deepcopy(inventory)
    for key in ls:
        if inventory[key]<=0:
            inventory.pop(key)

    return list(inventory.items())
    

    

