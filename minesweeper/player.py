class Player:
    """ Класс Игрока """
    def __init__(self, name):
        """
        Инициализирует игрока
        :param name: имя игрока.
        """
        self.name = name
        self.score = 0  # Счет игрока
        self.opened_cells = 0  # Количество открытых клеток

    def update_score(self):
        """ Увеличиваем счет за каждую открытую клетку. """
        self.score += 1
        self.opened_cells += 1

    def show_score(self):
        """ Показывает счет игрока и количество мин на поле. """
        print(f"Игрок: {self.name}, Счет: {self.score}")
