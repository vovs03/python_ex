# solution.py

def normalize_url(address):
    normal = address

    #############
    # CASE 1

    # prtcl = 'https://'
    # #if address[:8] != 'https://' or address[:7] != 'http://':
    # if address[:8] != 'https://':
    #     normal = prtcl + address
    # elif address[:7] == 'http://':
    # 	normal = prtcl + address[7:]
    
    # if address[:7] != 'http://'
    # 	normal = 
    # return normal

    # http:// 
    # return 'https://' + address[7:] if address[:7] != 'http://' or 

    #############
    # CASE 2

    """
    # Just // http://king
    if address[:7] == 'http://':
        # print("*** " * 5)
        # print('https://' + address[7:])

        normal = 'https://' + address[7:]

    # Just // kong
    elif address[:6] != 'http://' and address[:7] != 'https://':
        normal = 'https://' + address


    # Just // https://king-kong-film.cinema
    elif address[:7] == 'https://':
        normal = address[:]
        print("это норм")
    """ # 13:42

    #############
    # CASE 3

    prtcl = 'https://'
    #normal = prtcl + address

    # adr
    # kong !h !hs
    
    if address[:7] != 'http://' \
        and address[:8] != 'https://':
        normal = prtcl + address
    elif address[:7] == 'http://':
        normal = prtcl + address[7:]
    elif address[:8] == 'https://':
        normal = address
    # it's work 14:04

    return normal


print(normalize_url('kong'))
print(normalize_url('http://king'))
print(normalize_url('https://king-kong-film.cinema'))
