import pytest
from practice_pyscuffold.math_func import StudentDB

Ops = StudentDB

@pytest.fixture
def db(scope='module'):
    print('..........setup........')
    global db
    db = StudentDB()
    db.connect('data.json')
    yield db
    print('..........setup........')
    db.close()


def test_scott_data():
    db = StudentDB()
    db.connect('data.json')
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_mark_data():
    db = StudentDB()
    # db.connect('data.json')
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'

@pytest.mark.number
def test_calc_sum():
    assert Ops.calc_sum(2, 3) == 5

@pytest.mark.number
def test_multiply():
    assert Ops.multiply(2, 2) == 4

@pytest.mark.number
def test_divide():
    assert Ops.division(4, 2) == 2

@pytest.mark.string
def test_string():
    assert Ops.string('greet') == 'hello world'
    





