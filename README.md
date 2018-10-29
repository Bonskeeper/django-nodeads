# django_nodeads
Python\Django project.  
API endpoint "elements": 
- "http://127.0.0.1:8000/elements/" - displays a list of all saved and moderated elements.  
Elements can be added to the selected group, edited and deleted.

API endpoint "groups": 
- "http://127.0.0.1:8000/groups/" - displays a list of all saved groups.  
Groups can be added to the selected group, edited and deleted.  
The first group you add will be the root group.

API endpoint "child-groups":
- "http://127.0.0.1:8000/groups/pk/child_groups/" - displays all subgroups of the selected group(pk its group id)

API endpoint "child-elements":
- "http://127.0.0.1:8000/elements/pk/child_elements/" - displays all moderated elements of the selected group(pk its group id)

# Project terms.
Напишите приложение, которое будет иметь следующие модели:
1. Группы (иерархическая структура):
- родительская группа
- иконка (jpg/png-формат)
- название (64 символа)
- описание (512 символов)
- Вычисляемые поля:  
Количество дочерних групп  
Количество дочерних элементов

2. Элементы (принадлежат группам):
- родительская группа
- иконка (jpg/png-формат)
- название (64 символа)
- описание (512 символов)
- дата создания
- проверен модератором (null/true /false)

Все поля, кроме описания и родительской группы для группы, обязательны к заполнению.
- Создайте API, с помощью которого клиент сможет получать с сервера данные с вычисляемыми полями и совершать навигацию по группам, т.е. показывать содержимое каждой группы (дочерние группы и элементы). Добавьте пагинацию для этих запросов. В результатах запроса выдаются только те элементы, у которых значение поля "проверен модератором" равна true.  
Также из клиента пользователь должен иметь возможность с помощью API добавить новый элемент, который должен пройти модерацию в админке (запись добавляется со значением NULL для поля "проверен модератором"). 
Должна быть возможность входа в админку и наполнение контента через админку. Базу данных можете использовать любую(SQLite3, MySQL, PostgreSQL).

# Installation

1. Clone this repo (git clone https://github.com/Bonskeeper/django-nodeads.git)
2. Move to the project folder
3. From command line: pip install -r requirements.txt
4. From command line: python manage.py migrate
5. From command line: python manage.py loaddata db.json
6. From command line: python manage.py runserver
