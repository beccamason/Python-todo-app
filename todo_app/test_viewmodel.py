import pytest
from todo_app.Card import Card
from todo_app.ViewModel import ViewModel 
from todo_app.data import trello_items

@pytest.fixture
def board_prep(): 
    #Store current state of the board
    items = trello_items.get_items
    for item in items: 
        trello_items.remove_item(item.id)
    
    #Create new items 
    trello_items.add_item("Done Test", "DoneTest")
    trello_items.add_item("Doing Test", "DoingTest")
    trello_items.add_item("Not Started Test", "NotStartedTest")

    #Update status of done and doing items 
    for view_item in ViewModel.not_started_items: 
        if view_item.title == "Done Test":
            trello_items.complete_item(view_item.id)

        elif view_item.title == "Doing Test":
            trello_items.progress_item(view_item.id)
        
    added_items = trello_items.get_items
    
    #Remove added items 
    for added_item in added_items:
        trello_items.remove_item(added_item.id)

    #Restore board 
    for item in items: 
        trello_items.add_item(item.id)

def test_not_started():
    not_started = ViewModel.not_started_items
    for not_started_item in not_started: 
        assert not_started_item.status == "Not Started"

def test_doing(board_prep):
    assert(len(ViewModel.doing_items) == 1)

def test_done():
    assert(len(ViewModel.done_items) == 1)
