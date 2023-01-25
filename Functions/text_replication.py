"""
This module has a function to replicate text.

It is an example for static type checking.
"""

def text_replication(my_var: int = 2, my_text: str = 'Blah!') -> str:
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
    
    my_output = my_var * my_text
    
    return my_output


if __name__=='__main__':
    my_replication = text_replication(3, 'Hurrah!')
    print(my_replication)
    