import httpx 
from tools.fakers import fake 


payload = {
    "email": fake.email(),
    "password": "String123",
    "lastName": "Nurik",
    "firstName": "M",
    "middleName": "T"
}

response = httpx.post('http://localhost:8000/api/v1/users',json=payload)
print(response.json())
print(response.status_code)