import requests
api_url =  'https://jsonplaceholder.typicode.com/todos/1'

Items = {
    "name" : 'product name',
    "category" : 1,
    "price" : 20.5,
    "instock" : 200,
    "completed" : False
}

response = requests.get(api_url, json=Items)

print(response.json())
print(response.status_code)