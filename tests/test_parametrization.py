import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number",[1,2,3,-1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize("number, expected",[(1,1),(2,4), (3,9)])
def test_several_numbers(number: int,expected: int):
    assert number ** 2 == expected



@pytest.mark.parametrize("os",["macos","wondows","linux","debian"])
@pytest.mark.parametrize("host",[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def test_multiplication_of_numbers(os: str,host: str):
    assert len(os + host) > 0


@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def host(request: SubRequest) -> str:
    return request.param

def test_host(host: str):
    print(f"Running test on host: {host}")


@pytest.mark.parametrize("user",["Alice","Zara"])
class TestOperations:
    def test_user_with_operation(self, user: str):
        print(f"User with operation: {user}")
    def test_user_without_operation(self, user: str):
        print(f"User without operation: {user}")


users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operation on bank account"
}

@pytest.mark.parametrize(
        "phone_number",
            users.keys()
            ,
            ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
        )
def test_identifiers(phone_number: str):
    pass


@pytest.mark.parametrize(
    "input_value",
    [
        pytest.param(1, marks=pytest.mark.xfail(reason="Known issue with 1")),
        2,
        pytest.param(3, marks=pytest.mark.skip(reason="Feature not implemented for 3")),
    ]
)
def test_function999(input_value):
    assert input_value != 1