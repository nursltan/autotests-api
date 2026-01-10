from jsonschema import validate


schema = {
    "type": "object",
    "properties":{
        "name": {"type": "string"},
        "age": {"type": "number"}
    },
    "required": ["name"]
}

data = {
  "name": "John Doe",
  "age": 30
}

validate(data,schema)
