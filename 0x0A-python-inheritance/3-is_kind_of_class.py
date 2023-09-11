#!/usr/bin/python3



def is_kind_of_class(obj, a_class):
    """Check if an objects ia an instance
    Args:
        obj (any): object to check
    """
    if isinstance(obj, a_class):
        return True
    return False
