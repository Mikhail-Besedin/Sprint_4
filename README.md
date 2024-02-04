# qa_python_5 Sprint_4
Файл tests.py переименован в test_tests.py

### В файле main.py лежит приложение BooksCollector
#### В приложении есть следующие методы :
- add_new_book - добавляет новую книгу в словарь без указания жанра.
- set_book_genre - устанавливает жанр книги
- get_book_genre - выводит жанр книги по её имени.
- get_books_with_specific_genre - выводит список книг с определённым жанром.
- get_books_genre - выводит текущий словарь books_genre .
- get_books_for_children - возвращает книги, которые подходят детям.
- add_book_in_favorites - добавляет книгу в избранное.
- delete_book_from_favorites - удаляет книгу из избранного.
- get_list_of_favorites_books - получает список избранных книг.


### Для покрытия тестами BooksCollector разработаны следующие тесты: 

#### 1) test_add_new_book_add_two_books_collection_increased 
проверяет добавление двух книг 
  - Результат: 2 книги в словаре
#### 2) test_add_new_book_add_identical_books_add_one_book 
проверяет добавление двух одинаковых книг
  - Результат: добавлена только одна книга
#### 3) test_add_new_book_not_valid_name_empty_collection  
проверяет добавление книг с названием больше 40 символов 
  - Результат: книга не добавлена. 
#### 4) test_set_book_genre_add_genre_book_with_genre   
проверяет установку жанра книги 
  - Результат: жанр книге установлен 
#### 5) test_get_book_genre_add_book_with_genre_get_genre  
проверяет что по имени книги выводится жанр 
  - Результат: получен жанр книги 
#### 6) test_get_books_with_specific_genre_empty_list_add_two_books   
проверяет что выводится список книг по заданному жанру 
  - Результат: в выведенном списке 2 книги запрашиваемого жанра 
#### 7) test_get_books_for_children_empty_list_list_increased  
проверяет колличество добавленных книг, которые подходят детям по жанрам
  - Результат: добавлены все книги с соответсующими жанрами для детей 
#### 8) test_get_books_for_children_empty_list_only_children_genre  
проверяет что книги с возрастным рейтингом отсутствуют в списке книг для детей.
  - Результат: в списке книги только для детей 
#### 9) test_add_book_in_favorites_empty_list_list_increased 
проверяет добавление книги в избранное
  - Результат: Книга добавлена в избранное
#### 10) test_delete_book_from_favorites_add_two_book_list_decreased
проверяет удаление одной книги из списка 
  - Результат: Удалилась одна книга из 2х 


### Методы , на которые отдельно не писались тесты, но их покрывают выше указанные тесты: 
- get_books_genre
- get_list_of_favorites_books


Запустить все тесты + оценка покрытия  : 
```` bash
pytest -v test_tests.py
````
```` bash
pytest --cov=main
````
