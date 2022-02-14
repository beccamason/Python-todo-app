import pytest
from todo_app.Card import Card
from todo_app.ViewModel import ViewModel 
from todo_app.data import trello_items

@pytest.fixture
def board_prep(): 
    #Store current state of the board
    items = trello_items.get_items()
    for item in items: 
        trello_items.remove_item(item.id)
    
    #Create new items 
    trello_items.add_item("Done Test", "DoneTest")
    trello_items.add_item("Doing Test", "DoingTest")
    trello_items.add_item("Not Started Test", "NotStartedTest")

    #Update status of done and doing items 
    added_items = trello_items.get_items()
    trello_items.complete_item(added_items[0].id)
    trello_items.progress_item(added_items[1].id)
    added_items = trello_items.get_items()
    yield ViewModel(added_items)   
    
    #Remove added items 
    for added_item in added_items:
        trello_items.remove_item(added_item.id)

    #Restore board 
    for item in items: 
        trello_items.add_item(item.title, item.notes)

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
    assert board_prep.doing_items[0].title == "Doing Test"
    assert board_prep.doing_items[0].status == "In Progress"
    


