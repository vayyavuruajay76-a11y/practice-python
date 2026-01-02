"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    co=list([*args])
    return co


def fix_list_of_wagons(wagon_ids, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    reordered_wagons = wagon_ids[2:] + wagon_ids[:2]
    
    # Step 2: Find the index of the locomotive (ID 1)
    locomotive_index = reordered_wagons.index(1)
    
    # Step 3: Insert the missing wagons after the locomotive
    # We slice the list at the locomotive's position + 1 and insert the new list
    final_list = (
        reordered_wagons[:locomotive_index + 1] + 
        missing_wagons + 
        reordered_wagons[locomotive_index + 1:]
    )
    
    return final_list
    


def add_missing_stops(routing_dict, **kwargs):
    """
    Update the routing dictionary with a list of intermediary stops.
    
    :param routing_dict: dict - existing routing information.
    :param kwargs: variable number of stop_number=city keyword pairs.
    :return: dict - updated routing dictionary with an added "stops" list.
    """
    # Extract the values (city names) from the keyword arguments.
    # Because **kwargs preserves insertion order in modern Python, 
    # the stops will naturally be in the order they were passed.
    stops_list = list(kwargs.values())
    
    # Update the routing dictionary with the new "stops" key.
    routing_dict["stops"] = stops_list
    
    return routing_dict


def extend_route_information(route_base, additional_details):
    """
    Consolidates two dictionaries into one containing all routing information.
    """
    # Create a copy to avoid mutating the original input dictionary
    consolidated_route = route_base.copy()
    consolidated_route.update(additional_details)
    return consolidated_route

def fix_wagon_depot(wagon_rows):
    """
    Transposes the wagon grid so that each row contains one wagon of each color,
    ensuring that columns are aligned by color.
    """
    # zip(*wagon_rows) takes the three sublists and pairs their 
    # elements by index (0 with 0, 1 with 1, etc.)
    transposed = zip(*wagon_rows)
    
    # Convert the zip object back into a list of lists
    return [list(row) for row in transposed]
