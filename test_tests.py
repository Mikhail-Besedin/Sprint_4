import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books_collection_increased(self,collector):
        collector.add_new_book('Шоколадная фабрика')
        collector.add_new_book('Убийца дворецкий?')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_identical_books_add_one_book(self,collector):
        collector.add_new_book('Убийца дворецкий?')
        collector.add_new_book('Убийца дворецкий?')
        assert len(collector.get_books_genre()) != 2
    @pytest.mark.parametrize("name", ['Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции', 'Скажи мяу, ведьма, или Дом проклятых кошек'])
    def test_add_new_book_not_valid_name_empty_collection(self,collector,name):
        collector.add_new_book(name)
        assert collector.get_books_genre() == {}

    def test_set_book_genre_add_genre_book_with_genre(self,collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Ужасы')
        assert {'Что делать, если ваш кот хочет вас убить':'Ужасы'} == collector.get_books_genre()


    def test_get_book_genre_add_book_with_genre_get_genre(self,collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == 'Ужасы'

    def test_get_books_with_specific_genre_empty_list_add_two_books(self,collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы')==[
        'Что делать, если ваш кот хочет вас убить','Гордость и предубеждение и зомби']


    def test_get_books_for_children_empty_list_list_increased(self,collector):
        collector.add_new_book('Фиксики')
        collector.add_new_book('Шоколадная фабрика')
        collector.add_new_book('Клоун-дворецкий')
        collector.set_book_genre('Фиксики', 'Мультфильмы')
        collector.set_book_genre('Шоколадная фабрика', 'Фантастика')
        collector.set_book_genre('Клоун-дворецкий', 'Комедии')
        assert len(collector.get_books_for_children()) == 3

    @pytest.mark.parametrize("books_for_adults", ['Ужасы','Детективы'])
    def test_get_books_for_children_empty_list_only_children_genre(self,collector,books_for_adults):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Фиксики')
        collector.add_new_book('Шоколадная фабрика')
        collector.add_new_book('Убийца дворецкий?')
        collector.add_new_book('Клоун-дворецкий')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Фиксики', 'Мультфильмы')
        collector.set_book_genre('Шоколадная фабрика', 'Фантастика')
        collector.set_book_genre('Убийца дворецкий?', 'Детективы')
        collector.set_book_genre('Клоун-дворецкий', 'Комедии')
        for name in collector.get_books_for_children():
            assert name not in collector.get_books_with_specific_genre(books_for_adults)


    def test_add_book_in_favorites_empty_list_list_increased(self,collector):
        collector.add_new_book('Убийца дворецкий?')
        collector.set_book_genre('Убийца дворецкий?', 'Детективы')
        collector.add_book_in_favorites('Убийца дворецкий?')
        assert collector.get_list_of_favorites_books() == ['Убийца дворецкий?']

    def test_delete_book_from_favorites_add_two_book_list_decreased(self,collector):
        collector.add_new_book('Фиксики')
        collector.add_new_book('Убийца дворецкий?')
        collector.set_book_genre('Фиксики', 'Мультфильмы')
        collector.set_book_genre('Убийца дворецкий?', 'Детективы')
        collector.add_book_in_favorites('Убийца дворецкий?')
        collector.add_book_in_favorites('Фиксики')
        collector.delete_book_from_favorites('Убийца дворецкий?')
        assert collector.get_list_of_favorites_books() ==['Фиксики']


