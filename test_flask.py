import requests


def func(url):
    r = requests.get(url)
    return r.status_code


def test_Tasks():
    assert func('http://localhost:5000/todo/api/v1.0/tasks') == 200


def test_Task():
    assert func('http://localhost:5000/todo/api/v1.0/tasks/1') == 200


if __name__ == '__main__':
    test_Tasks()
    test_Task()
