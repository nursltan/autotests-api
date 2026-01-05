import httpx


# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')

# print(response.status_code)
# print(response.json())


# data = {
#     "title": "New Task",
#     "completed": False,
#     "userId": 1
# }

# response = httpx.post('https://jsonplaceholder.typicode.com/todos',json=data)

# print(response.status_code)
# print(response.json())


# data = {"username":"Kolya", "password": "123456"}

# response = httpx.post('https://httpbin.org/post', data=data)

# print(response.status_code)
# print(response.json())



# headers = {"Authorization": "Bearer my_secret_key"}
# response = httpx.get('https://httpbin.org/get',headers=headers)

# print(response.request.headers)
# print(response.json())

# params = {"userId": 3}
# response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)

# print(response.status_code)
# print(response.json())



# files = {"file": ("example.txt", open("examples/example.txt", "rb"))}
# response = httpx.post('https://httpbin.org/post', files=files)
# print(response.status_code)
# print(response.json())


# with httpx.Client():
#     response1 = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
#     response2 = httpx.get('https://jsonplaceholder.typicode.com/todos/2')

# print(response1.json())
# print(response2.json())


# client = httpx.Client(headers={"Authorization": "Bearer my_secret_key"})
# response = client.get('https://httpbin.org/get')
# print(response.json())

# try:
#     response = httpx.get('https://jsonplaceholder.typicode.com/invalid-url')
#     response.raise_for_status()
# except httpx.HTTPStatusError as e:
#     print(f'Ошибка в запросе: {e}')


try:
    response = httpx.get('https://httpbin.org/delay/1', timeout=2)
except httpx.ReadTimeout:
    print('Таймаут')