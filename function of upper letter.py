def longmaj(password) :
    max_length = 0
    current_length = 0
    for char in password :
        if "A" <= char <= "Z" :
            current_length += 1
        else :
            current_length = 0
        if max_length < current_length :
            max_length = current_length
    return(max_length)