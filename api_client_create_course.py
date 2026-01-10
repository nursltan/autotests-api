from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_client import get_files_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.files.files_schema import CreateFileRequestSchema
from tools.fakers import fake


public_user_client = get_public_users_client()
# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
# Используем метод create_user
create_user_response = public_user_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)


create_file_request = CreateFileRequestSchema(
    filename="4.png",
    directory="courses",
    upload_file="./testdata/files/2.png"
)

create_file_response = files_client.create_file(create_file_request)
print("Create file data: ",create_file_response)


create_course_request = CreateCourseRequestSchema(
    title="Python 1",
    max_score=100,
    min_score=10,
    description="Python Api courses",
    preview_file_id=create_file_response.file.id,
    estimated_time="2 weeks",
    created_by_user_id=create_user_response.user.id
)

create_course_response = courses_client.create_course(create_course_request)
print("Create course data: ", create_course_response)