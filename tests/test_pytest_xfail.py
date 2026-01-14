import pytest


@pytest.mark.xfail(reason="Найден баг в приложении, из-за которого тест падает ошибкой")
def test_with_bug():
    assert 1==2

@pytest.mark.xfail(reason="Баг уже исправлен, но на тесте все еще висит маркеровка xfail")
def test_without_bug():
    ...

@pytest.mark.xfail(reason="Внешний сервис временно недоступен")
def test_service_unaviable():
    assert 1==2