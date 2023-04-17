class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if input_list:
            max_elem = input_list[0]

            for elem in input_list:
                if elem > max_elem:
                    max_elem = elem

            output_list = []

            for elem in input_list:
                if elem > 0:
                    output_list.append(max_elem)
                else:
                    output_list.append(elem)

            return output_list
        return input_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        low = 0
        high = len(input_list) - 1

        def binary_search_recursive(input_list: list[int], query: int, low: int, high: int) -> int:
            if low > high:
                return -1

            mid = (low + high) // 2
            if query == input_list[mid]:
                return mid

            if query < input_list[mid]:
                return binary_search_recursive(input_list, query, low, mid - 1)
            else:
                return binary_search_recursive(input_list, query, mid + 1, high)

        return binary_search_recursive(input_list, query, low, high)
