import requests
request_headers = {
    'User-Agent': 'Holberton_School',
    'Authorization':'token 6e7f3146a1a9d7a12e4aceac3f3918c2fa57be6a'
}
r = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc')
r.text
