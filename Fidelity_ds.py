def segregate(l):
    """This function returns list with only integers. It takes a list as argument"""
    return [i for i in l if isinstance(i, int)]