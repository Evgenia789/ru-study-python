from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        """
        Реализовать функцию, которая ведет себя как filter и map. К каждому значению из
        списка применяется функция, которая в ответ возвращает кортеж
        (булево значение, результат работы функции).
        Если первый элемент кортежа истина, то результат добавляется в список.

        Принимает в качестве аргументов функцию и итерируемый источник, а возвращает список.
        :param func: Функция, применяемая к каждому элементу списка.
        :param input_array: Исходный список.
        :return: Отфильтрованный список.
        """
        filter_array = []

        for elem in input_array:
            is_valid, res = func(elem)
            if is_valid:
                filter_array.append(res)

        return filter_array
