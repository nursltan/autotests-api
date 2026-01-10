import httpx 
from tools.fakers import fake 


create_user_payload = {
    "email": fake.email(),
    "password": "String123",
    "lastName": "Nurik",
    "firstName": "M",
    "middleName": "T"
}

create_user_response = httpx.post('http://localhost:8000/api/v1/users',json=create_user_payload)
create_user_data = create_user_response.json()
print('Данные созданного пользователя: ', create_user_data)
print('Статус код создания пользователя: ', create_user_response.status_code)


login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login',json=login_payload)
login_response_data = login_response.json()

print('Данные авторизации: ',login_response_data)
print('Статус код авторизации: ', login_response.status_code)


delete_user_headers = {'Authorization': f'Bearer {login_response_data['token']['accessToken']}'}

delete_user_response = httpx.delete(f'http://localhost:8000/api/v1/users/{create_user_data['user']['id']}',headers=delete_user_headers)

print('Статус код удаления: ', delete_user_response.status_code)