import os

from game_pole import GamePole
from player import Player

print('Приветствуем вас в игре САПЕР!'
      '\nИгровое поле будет отображено, и вы увидите свой текущий счет и количество мин на поле. '
      '\nВводите координаты клетки, которую хотите открыть, в формате x y (например, 3 4).'
      '\nЕсли вы хотите выйти из игры в любой момент, введите exit.  '
      '\nЕсли вы откроете клетку с миной, игра закончится.  '
      '\nЕсли вы откроете все безопасные клетки, вы выиграете!'
      '\nУДАЧИ!')

player_name = input("Введите ваше имя: ")
N = int(input("Введите размер поля: "))
M = int(input("Введите оличество мин: "))
player = Player(player_name)

game = GamePole(N, M)
# game = GamePole(10, 10)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Очистка консоли перед отображением поля
    game.show()
    player.show_score()
    user_input = input("Введите координаты (x y) или 'exit' для выхода: ")

    if user_input.lower() == 'exit':
        print("Вы вышли из игры. Спасибо за игру!")
        break

    try:
        x, y = map(int, user_input.split())
        game.open_cell(x, y)
        if not game.open_cell(x, y):
            print("Вы попали на мину! Игра окончена.")
            break
        player.update_score()  # Обновляем счет, если клетка открыта успешно
        if player.opened_cells == game.safe_cells_count:
            print("Поздравляем! Вы выиграли!")
            break
    except (ValueError, IndexError):
        print("Некорректный ввод. Попробуйте снова.")
player.show_score()
