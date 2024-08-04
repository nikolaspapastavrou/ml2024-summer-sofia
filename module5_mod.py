class NumberSearcher:

    def __init__(self):
        self.numbers_to_search = []

    def populate_numbers(self):
        number_of_inputs_to_read = ""
        while not NumberSearcher._is_positive_int(number_of_inputs_to_read):
            number_of_inputs_to_read = input("Please insert a positive integer number for the number of numbers to read: ")

        number_of_inputs_to_read = int(number_of_inputs_to_read)
        for _ in range(number_of_inputs_to_read):
            read_input = ""
            while not NumberSearcher._is_float(read_input):
                read_input = input("Please insert a valid number (integer, floating point, or negative): ")
            self.numbers_to_search.append(float(read_input))

    def search_numbers(self):
        target_value = ""
        while not NumberSearcher._is_float(target_value):
            target_value = input("Please insert a valid integer number (positive or negative) to search for in the existing numbers: ")

        for i, current_number in enumerate(self.numbers_to_search):
            if float(current_number) == float(target_value):
                print(i+1)
                return

        print(-1)

    @staticmethod
    def _is_float(input_value: str):
        try:
            _ = float(input_value)
        except Exception:
            return False
        return True

    @staticmethod
    def _is_int(input_value: str):
        return NumberSearcher._is_float(input_value) and (input_value.isnumeric() or (input_value[0] == '-' and input_value[1:].isnumeric()))

    @staticmethod
    def _is_positive_int(input_value: str):
        return NumberSearcher._is_int(input_value) and (float(input_value) > 0)
