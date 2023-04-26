def normalize_url(url):

    https = 'https://'
    
    #Check HTTPS_ADDRESS
    if url[:8] == 'https://':
        return url

    #Check HTTP_ADDRESS
    elif url[:7] == 'http://':
        return https + url[7:]

    #Check ADDRESS
    else:
        return https + url
    

print(normalize_url('kong'))
print(normalize_url('http://king'))
print(normalize_url('https://king-kong-film.cinema'))
