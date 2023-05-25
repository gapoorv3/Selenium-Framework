import pytest


@pytest.fixture()
def test_setup():
    print('first')
    yield
    print('second')

def test_main(test_setup):
    print('real test')

# print('f')
