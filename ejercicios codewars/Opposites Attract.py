def lovefunc( flw1, flw2 ):
    if flw1 % 2 == 0 and flw2 % 2 != 0:
        return(True)
    
    elif flw1 % 2 != 0 and flw2 % 2 == 0:
        return(True)
    
    else:
        return(False)