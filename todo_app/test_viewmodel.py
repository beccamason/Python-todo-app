import pytest
from todo_app.Card import Card
from todo_app.ViewModel import ViewModel 
from todo_app.data import trello_items

@pytest.fixture
def board_prep(): 
    not_started_card = Card("1", "Not Started Test", "Not Started", "test")
    in_progress_card = Card("2", "In Progress Test", "In Progress", "test")
    done_card = Card("3", "Done Test", "Done", "test")
    cards = [not_started_card, in_progress_card, done_card]
    return ViewModel(cards)

@pytest.fixture
def done_cards_prep():
    done_card_1 = Card("3", "Done Test", "Done", "test")
    done_card_2 = Card("4", "Done Test", "Done", "test")
    done_card_3 = Card("5", "Done Test", "Done", "test")
    done_card_4 = Card("6", "Done Test", "Done", "test")
    done_card_5 = Card("7", "Done Test", "Done", "test")
    done_card_6 = Card("8", "Done Test", "Done", "test")
    done_cards = [done_card_1, done_card_2, done_card_3, done_card_4, done_card_5, done_card_6]
    return ViewModel(done_cards)

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

def test_done_length(done_cards_prep):
    if len(board_prep.done_items) > 5: 
        assert len(board_prep.done_items_filtered) == 5
    else: assert(True)
