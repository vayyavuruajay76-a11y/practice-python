"""Functions to manage a users shopping cart items."""
import copy

def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for index,value in enumerate(items_to_add):
        if value in current_cart.keys():
            current_cart[value]+=1
        else:
            current_cart.setdefault(value,1)

    return current_cart

    


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    shopping_cart={}
    for index,value in enumerate(notes):
        if value in shopping_cart.keys():
            shopping_cart[value]+=1
        else:
            shopping_cart.setdefault(value,1)


    return shopping_cart

    


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    updated_ideas = ideas.copy()
    
    for recipe_name, new_ingredients in recipe_updates:
        updated_ideas[recipe_name] = new_ingredients
        
    return updated_ideas
            
            
            

    


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    ls=dict(sorted(cart.items()))
    return ls

    


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    updated_cart=cart.copy()
    for key,value in cart.items():
        if key in aisle_mapping.keys():
            a=value
            aisle_mapping[key].insert(0,a)
            updated_cart[key]=aisle_mapping[key]

    ls=dict(sorted(updated_cart.items(),reverse=True))

    return ls

    

    

    


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    updated_inventory=store_inventory.copy()
    for item,(ordered_qty,*_) in fulfillment_cart.items():
        if item in updated_inventory.keys():
            current_qty=updated_inventory[item][0]
            updated_qty=current_qty-ordered_qty
            if updated_qty<=0:
                updated_inventory[item]=['Out of Stock']+updated_inventory[item][1:]
            else:
                updated_inventory[item]=[updated_qty]+updated_inventory[item][1:]

    return updated_inventory
        
            
            

    
