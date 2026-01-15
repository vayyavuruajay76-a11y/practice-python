"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seat_map = ['A', 'B', 'C', 'D']
    count = 0
    while count < number:
        # Use the modulo operator (%) to cycle through the seat_map list
        yield seat_map[count % 4]
        count += 1

    


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    row = 1
    seat_letters = ["A", "B", "C", "D"]
    count = 0
    
    while count < number:
        # Skip row 13 due to superstition
        if row == 13:
            row += 1
            
        for letter in seat_letters:
            if count >= number:
                return
            yield f"{row}{letter}"
            count += 1
            
        row += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat_generator = generate_seats(len(passengers))
    
    assignments = {}
    for person in passengers:
        # Pair the passenger with the next available seat from the generator
        assignments[person] = next(seat_generator)
        
    return assignments

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        # Combine seat and flight_id
        base_code = f"{seat}{flight_id}"
        
        # Pad with '0' until the string reaches 12 characters
        # .ljust(12, '0') adds the character '0' to the right side
        yield base_code.ljust(12, '0')

