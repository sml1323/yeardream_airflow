import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = '1c6bcbde2a6eefae86fc651c07e010e1'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'HnWN9SiUbT7qd90pvYmt1R5IpZeIFmHL5Q3F3T-BufWwpD_oFxULkQAAAAQKPXUbAAABkC4A2rJSGUcvaFb1Eg'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)