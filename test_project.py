import project
import pytest



def main():
    test_book_number_validator()
    test_menu_number_validator()
    test_view_books()


def test_book_number_validator():
    assert project.book_number_validator("One") == False
    assert project.book_number_validator("1") == False


def test_menu_number_validator():
    assert project.menu_number_validator("Two") == False
    assert project.menu_number_validator("8") == False
    assert project.menu_number_validator("3") == True
    with pytest.raises(SystemExit):
        assert project.menu_number_validator("7")


def test_view_books():
    assert project.view_books() == "You have 0 books in book tracker. Feel free add some :)\n"
