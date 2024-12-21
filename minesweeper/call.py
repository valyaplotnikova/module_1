class Call:
    """
    Класс для представления клетки игрового поля.
    С помощью этого класса создаются отдельные клетки игрового поля.
    """

    def __init__(self, around_mines=0, mine=False):
        """
        Инициализатор клетки игрового поля
        :param around_mines: число мин вокруг данной клетки;
        :param mine: наличие/отсутствие мины в текущей клетке;
        :param: fl_open: открыта/закрыта клетка.
        """

        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False
