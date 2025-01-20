"""4 задание
Написать функцию, которая получает на вход список словарей, содержащих информацию о фильмах
(например, название, жанр, режиссер и т. д.), и возвращает новый список,
содержащий только те фильмы, которые относятся к заданному жанру.
Пример ввода:
[{title: 'The Shawshank Redemption', genre: 'Drama', director: 'Frank Darabont'},
{title: 'The Godfather', genre: 'Crime', director: 'Francis Ford Coppola'},
{title: 'The Dark Knight', genre: 'Action', director: 'Christopher Nolan'}], 'Drama'

Пример вывода:
[{title: 'The Shawshank Redemption', genre: 'Drama', director: 'Frank Darabont'}]
"""

def films_equal_to_genres(new_list, new_gener):
    result = []
    for i in new_list:
        if i['genre'] == new_gener:
            result.append(i)

    return result



list_new = [
    {'title': 'The Shawshank Redemption', 'genre': 'Drama', 'director': 'Frank Darabont'},
    {'title': 'The Godfather', 'genre': 'Crime', 'director': 'Francis Ford Coppola'},
    {'title': 'The Dark Knight', 'genre': 'Action', 'director': 'Christopher Nolan'}
],
gener_new = 'Drama'

print(films_equal_to_genres(list_new, gener_new))