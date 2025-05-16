import math

def distance_squared(loc1, loc2):
    """
    Calculate the squared distance between two location tuples.
    """
    x1, y1 = loc1
    x2, y2 = loc2
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

def turn_heading(current_heading, target_heading, max_turn=None):
    """
    Calculate the new heading after turning towards a target heading.
    
    Parameters:
    current_heading: Current heading in degrees (0-359)
    target_heading: Target heading in degrees (0-359)
    max_turn: Maximum allowed turn in degrees (optional)
    
    Returns:
    float: The new heading after the turn
    """
    # Normalize headings to 0-359 range
    current_heading = current_heading % 360
    target_heading = target_heading % 360
    
    # Calculate the difference
    diff = target_heading - current_heading
    
    # Adjust for the shortest path
    if diff > 180:
        diff -= 360
    elif diff < -180:
        diff += 360
    
    # Apply maximum turn constraint if specified
    if max_turn is not None:
        if diff > max_turn:
            diff = max_turn
        elif diff < -max_turn:
            diff = -max_turn
    
    # Calculate and normalize the new heading
    new_heading = (current_heading + diff) % 360
    
    return new_heading