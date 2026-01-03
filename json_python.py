import json

data = {
    'name': 'Мария',
    'age': 19,
    'is_student': True
}
with open("json_example.json",'r',encoding="utf-8") as file:
    read_data = json.load(file)
    print(read_data)

with open('json_user.json','w',encoding='utf-8') as file:
    json.dump(data,file,indent=2,ensure_ascii=False)