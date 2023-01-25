def tryexceptelsefinally(in_var):
    
    try:
        if in_var >= 5:
            raise        
    except:
        in_var = in_var + 2
    else:
        in_var = in_var - 3
    finally:
        in_var += 1
        
    return in_var