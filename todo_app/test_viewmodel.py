import pytest
from todo_app.Card import Card
from todo_app.ViewModel import ViewModel 
from todo_app.data import trello_items

@pytest.fixture
def board_prep(): 
    cards = [Card("1", "Not Started Test", "Not Started", "test"), Card("2", "In Progress Test", "In Progress", "test"), Card("3", "Done Test", "Done", "test")]
    return ViewModel(cards)

def test_pytest(): 
    assert(True)

def test_not_started(board_prep):
    assert len(board_prep.not_started_items) == 1
    assert board_prep.not_started_items[0].title == "Not Started Test"
    assert board_prep.not_started_items[0].status == "Not Started"
    
def test_done(board_prep):
    assert len(board_prep.done_items) == 1
    assert board_prep.done_items[0].title == "Done Test"
    assert board_prep.done_items[0].status == "Done"  

def test_doing(board_prep):
    assert len(board_prep.doing_items) == 1
    assert board_prep.doing_items[0].title == "In Progress Test"
    assert board_prep.doing_items[0].status == "In Progress"