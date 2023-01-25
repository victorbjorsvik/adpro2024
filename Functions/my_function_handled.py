def my_func(my_var: int = 2, my_text: str = 'Blah!') -> str:
    """
    Replicates a string assigned in 'my_text' a number of times in 'my_var'
    
    Parameters
    ---------------
    my_var: int
        The number of times to replicate the input string
    my_text: string
        The string to be replicated
        
    Returns
    ---------------
    my_output: string
        The 'my_text' string replicated 'my_var' times
    
    """
    
    if type(my_var) != int:
        raise TypeError("Variable 'my_var' is not int.")
        
    if type(my_text) != str:
        raise TypeError("Variable 'my_text' is not string.")

    
    my_output = my_var * my_text
    
    return my_output