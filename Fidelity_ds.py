def segregate(l):
    """This function returns list with only integers. It takes a list as argument"""    # this is the documentation to help users
    return [i for i in l if isinstance(i, int)]