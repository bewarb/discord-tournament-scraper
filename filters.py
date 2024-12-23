# filters.py

def filter_by_date(tournaments, date):
    """
    Filters tournaments by a specific date.
    """
    return [t for t in tournaments if t["date"] == date]

def filter_by_type(tournaments, type_):
    """
    Filters tournaments by a specific type (e.g., RCO, COED).
    """
    return [t for t in tournaments if t["type"].lower() == type_.lower()]

def filter_by_location(tournaments, location):
    """
    Filters tournaments by location.
    """
    return [t for t in tournaments if t["location"].lower() == location.lower()]

def filter_tournaments(tournaments, **kwargs):
    """
    Applies multiple filters to the list of tournaments.
    
    Args:
        tournaments (list): List of tournament dictionaries.
        kwargs (dict): Dictionary of filters to apply.
            Supported filters: 'date', 'type', 'location'

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
    return filtered
