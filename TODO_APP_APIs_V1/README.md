# Author: Ahmed Shrief Ramadan

## Time spent: Few days

## Challenges

- Leak of resources for DRF.
- There's no clear steps to follow.
- There are many details in this topic so it took much time.

## Resources

[DRF tutorial](https://www.django-rest-framework.org/)

Many videos.

## About the project

- Implement almost the all method of views:

1. Function Based View (FBV)
2. Class Based View (CBV)
3. Mixins
4. Generics
5. View-Sets

- Implement 2 Serializers:

1. For CustomUser model
2. For ListItem model

- Implement Search and filters in View-Sets for example:

`http://127.0.0.1:8000/rest/viewsets/items/?search=fourth` If you want to **Search** for certian item by just item field.

`http://127.0.0.1:8000/rest/viewsets/items/?status=Finished` If you want to **Filter** by status.

There's is function called `all_items_for_user` To get the all items of specific user.

- All other implementations **(List , Create)** and **(GET , PUT , DELETE)** with pk.

## Note: You must read urls.py in todo_app dir to know how to send request correctly
