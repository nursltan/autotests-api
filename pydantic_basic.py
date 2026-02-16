"""
{
  "courses": [
    {
      "id": "string",
      "title": "string",
      "maxScore": 0,
      "minScore": 0,
      "description": "string",
      "previewFile": {
        "id": "string",
        "filename": "string",
        "directory": "string",
        "url": "https://example.com/"
      },
      "estimatedTime": "string",
      "createdByUser": {
        "id": "string",
        "email": "user@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
      }
    }
  ]
}
"""
import uuid
from pydantic import BaseModel, Field, ConfigDict, ValidationError, computed_field, EmailStr, HttpUrl
from pydantic.alias_generators import to_camel


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field
    def user_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    def get_user_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

class CoursesSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "playwright"
    max_score: int = Field(alias="maxScore",default=1000)
    min_score: int = Field(alias="minScore", default=10)
    description: str = "playwright"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime",default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")




course_default_model = CoursesSchema(
    id="course-id",
    title="playwright",
    maxScore=100,
    minScore=10,
    description="playwright",
    previewFile=FileSchema(
        id="file-id",
        filename="1.png",
        directory="courses",
        url="http://localhost:8000"
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(
        id="user-id",
        email="test@example.com",
        lastName="User1",
        firstName="test",
        middleName="TEEST"
    )
)

print("courses default model:",course_default_model)

course_dict = {
      "id": "course-id",
      "title": "playwright",
      "maxScore": 100,
      "minScore": 10,
      "description": "playwright",
      "previewFile": {
        "id": "file-id",
        "filename": "1.png",
        "directory": "courses",
        "url": "http://localhost:8000"
      },
      "estimatedTime": "1 week",
      "createdByUser": {
        "id": "user-id",
        "email": "test@example.com",
        "lastName": "User1",
        "firstName": "test",
        "middleName": "TEEST"
      }
    }

course_dict_model = CoursesSchema(**course_dict)

print("Course dict:",course_dict_model)

course_json = """
{
      "id": "course-id",
      "title": "playwright",
      "maxScore": 100,
      "minScore": 10,
      "description": "playwright",
      "previewFile": {
        "id": "file-id",
        "filename": "1.png",
        "directory": "courses",
        "url": "http://localhost:8000"
      },
      "estimatedTime": "1 week",
      "createdByUser": {
        "id": "user-id",
        "email": "test@example.com",
        "lastName": "User1",
        "firstName": "test",
        "middleName": "TEEST"
      }
}
"""
course_json_model = CoursesSchema.model_validate_json(course_json)
print("Course JSON model:",course_json_model)
print(course_default_model.model_dump(by_alias=True))
print(course_default_model.model_dump_json(by_alias=True))


user = UserSchema(
        id="user-id",
        email="test@example.com",
        lastName="User1",
        firstName="test",
        middleName="TEEST"
    )
print(user.get_user_name(), user.user_name)


try:
  file=FileSchema(
    id="file-id",
    filename="1.png",
    directory="courses",
    url="localhost"
  )
except ValidationError as error:
    print(error)
    print(error.errors())