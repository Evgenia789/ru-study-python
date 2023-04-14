from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """
        def check_countries_and_rating(movie: dict) -> Union[int, None]:
            if "," in movie["country"] and movie["rating_kinopoisk"]:
                if (ratings := float(movie["rating_kinopoisk"])) > 0:
                    return ratings
            return None

        ratings = [
            rating
            for rating in map(lambda x: check_countries_and_rating(x), list_of_movies)
            if rating is not None
        ]
        sum_ratings = sum(ratings)
        avg_ratings = sum_ratings / len(ratings)

        return avg_ratings

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """
        def count_letter(title: str) -> int:
            count = 0
            for letter in title:
                if letter == "и":
                    count += 1
            return count

        def check_rating(movie: dict) -> bool:
            if movie["rating_kinopoisk"] and float(movie["rating_kinopoisk"]) >= rating:
                return count_letter(movie["name"])
            return 0

        result = sum([count for count in map(lambda x: check_rating(x), list_of_movies)])

        return result
