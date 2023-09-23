import urllib.request

def url_chck():
    
    url_input = input('Enter the url you want to check: ')

    if not url_input.startswith(('http://', 'https://')):
        url_input = 'https://' + url_input

    print('Checking connection...')
    
    try:
        response = urllib.request.urlopen(url_input)
        result = response.getcode()
        if result == 200:
            print('Site is up and running!')
        else:
            print('Error!')
    except Exception as e:
        print('Error! Please check url or site is down.')


url_chck()