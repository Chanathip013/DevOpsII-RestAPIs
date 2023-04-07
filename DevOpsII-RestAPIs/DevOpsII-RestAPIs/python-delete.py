import requests
api_url =  'https://jsonplaceholder.typicode.com/todos/909'
# api_url =  'https://api.github.com/users/Chanathip013'

response = requests.delete(api_url)
print(response.json())
print(response.status_code)