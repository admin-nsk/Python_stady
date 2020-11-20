#!/usr/bin/python3

from functools import reduce


class BowlingScore:
    def __init__(self):
        self.result = 0

    def get_score(self, game_result):
        if self._check_input_data(game_result):
            self.result = reduce(lambda x, y: x + y, self._calc_score(game_result))
        return self.result

    def _check_input_data(self, game_result):
        """Check input result"""
        if not game_result:
            raise ValueError("Передан пустой результат")
        elif type(game_result) != str:
            raise TypeError("Неверный тип результата")
        elif 3 > len(game_result) or len(game_result) > 6:
            raise SyntaxError("Некорректная длина данных")
        elif list(game_result).count('/') > 3:
            raise SyntaxError("Spare не может быть больше 3х раз")
        elif list(game_result).count('X') > 3:
            raise SyntaxError("Strike не может быть больше 3х раз")
        elif game_result.find("//") != -1:
            raise SyntaxError("Spare не может быть подряд //")
        elif game_result.find("X/") != -1:
            raise SyntaxError("Spare не может идти после Strike X/")
        elif game_result[game_result.find("X")+2] == "X" and game_result != "XXX":
            raise SyntaxError(f"Не корректный синтаксис {game_result}")
        elif not self._check_frame(game_result):
            raise SyntaxError(f"Некоррекное количество фреймов {game_result}")
        else:
            return True

    def _calc_score(self, game_result):
        """ Calculation score"""
        next_i = 0
        while next_i < len(game_result):
            if game_result[next_i] == "X":
                yield 20
            elif next_i+1 != len(game_result) and game_result[next_i + 1] == "/":
                next_i += 1
                yield 15
            elif game_result[next_i] == "-":
                yield 0
            elif game_result[next_i].isdigit():
                yield int(game_result[next_i])
            else:
                raise ValueError(f'Неизвестный символ {game_result[next_i]}')
            next_i += 1

    def _check_frame(self, game_result):
        """Count input frame"""
        _count_x = list(game_result).count("X")
        if _count_x + len(game_result) != 6:
            return False
        else:
            return True


if __name__ == '__main__':
    bowling = BowlingScore()
    result = bowling.get_score("555555")
    print(result)
