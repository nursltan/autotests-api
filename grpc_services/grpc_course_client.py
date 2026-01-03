import grpc

import generated.course_service_pb2 as course_service_pb2
import generated.course_service_pb2_grpc as course_service_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = course_service_pb2_grpc.CourseServiceStub(channel)
        request = course_service_pb2.GetCourseRequest(course_id="api-course")
        response = stub.GetCourse(request)
        print(response)


if __name__ == "__main__":
    run()
