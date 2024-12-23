def filter_by_date(tournaments, date):
    """
    Filters tournaments by a specific date.
    
    Args:
        tournaments (list): List of tournament dictionaries.
        date (str): Date to filter by (e.g., '12/21/24').

    Returns:
        list: Filtered tournaments matching the date.
    """
    return [t for t in tournaments if t["date"] == date]

def filter_by_type(tournaments, type_):
    """
    Filters tournaments by a specific type (e.g., RCO, COED).

    Args:
        tournaments (list): List of tournament dictionaries.
        type_ (str): Type to filter by (e.g., 'RCO').

    Returns:
        list: Filtered tournaments matching the type.
    """
    return [t for t in tournaments if t["type"].lower() == type_.lower()]

def filter_by_location(tournaments, location):
    """
    Filters tournaments by location.

    Args:
        tournaments (list): List of tournament dictionaries.
        location (str): Location to filter by (e.g., 'TUH').

    Returns:
        list: Filtered tournaments matching the location.
    """
    return [t for t in tournaments if t["location"].lower() == location.lower()]

def filter_by_roles(tournaments, allowed_types):
    """
    Filters tournaments based on allowed types derived from user roles.

    Args:
        tournaments (list): List of tournament dictionaries.
        allowed_types (list): List of tournament types to filter by (e.g., ['M', 'RCO']).

    Returns:
        list: Filtered list of tournaments matching the allowed types.
    """
    return [t for t in tournaments if t["type"] in allowed_types]

def filter_tournaments(tournaments, **kwargs):
    """
    Applies multiple filters to the list of tournaments.

    Args:
        tournaments (list): List of tournament dictionaries.
        kwargs (dict): Dictionary of filters to apply.
            Supported filters: 'date', 'type', 'location', 'roles'

    Returns:
        list: Filtered list of tournaments.
    """
    filtered = tournaments
    if "date" in kwargs and kwargs["date"]:
        filtered = filter_by_date(filtered, kwargs["date"])
    if "type" in kwargs and kwargs["type"]:
        filtered = filter_by_type(filtered, kwargs["type"])
    if "location" in kwargs and kwargs["location"]:
        filtered = filter_by_location(filtered, kwargs["location"])
    if "roles" in kwargs and kwargs["roles"]:
        filtered = filter_by_roles(filtered, kwargs["roles"])
    return filtered

def filter_top_by_date(tournaments, top_n=10):
    """
    Sorts tournaments by date and limits the output to the top N closest tournaments.

    Args:
        tournaments (list): List of tournament dictionaries.
        top_n (int): Number of tournaments to return (default is 10).

    Returns:
        list: Sorted and limited list of tournaments.
    """
    return sorted(tournaments, key=lambda x: x["date"])[:top_n]
