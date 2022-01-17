import random
import keyboard

# Блокировка клавиш Alt, Ctrl, Tab
keyboard.block_key("ctrl")
keyboard.block_key("alt")
keyboard.block_key("tab")


# Функция безопасного ввода
def safe_input():
    string = input('\nВведите матрицу в одну строку, разделяя строки матрицы пробелом:\n')
    if not (string.count(' ') == 3):  # Проверяем, разделена ли строка пробелами для дальнейшего разделения
        spaces_expection()  # Уведомляем пользователя об ошибке
    else:
        if not check_only_digits(string):  # Проверяем, только ли цифры используются в записи строки
            not_all_isdigits()  # Уведомляем пользователя об ошибке
        else:
            matrix = string.split()  # Создаем список, разделяя строку по пробелам
            four_rows = check_rows(matrix)  # Узнаем, соответствует ли количество строк заявленному в варианте
            four_cols = check_cols(matrix)  # Узнаем, соответствует ли количество столбцов заявленному в варианте
            if not (four_rows and four_cols):  # Проверяем соответствие размера матрицы
                invalid_rows_and_cols_count()  # Уведомляем пользователя об ошибке
            else:
                # Создаем список чисел из исходной строки
                matrix = list(map(lambda str: list(map(int, str)), string.split()))
                start_program(matrix)  # Запускаем основной алгоритм программы (в соответствии с вариантом)


# Функции проверок
def check_rows(matrix):
    if len(matrix) == 4:
        return True
    return False


def check_cols(matrix):
    for m in matrix:
        if len(m) != 4:
            return False
    return True


def check_only_digits(string):
    for s in string:
        if not (s.isdigit() or s == ' '):
            return False
    return True


# Функции отображения ошибок
def spaces_expection():
    print('\nНужно разделять строки матрицы пробелами!\nЛибо введено недостаточное количество пробелов!\n')
    safe_input()


def invalid_rows_and_cols_count():
    print('\nНеправильные размеры матрицы, повторите ввод\n')
    safe_input()


def not_all_isdigits():
    print('\nНе все элементы матрицы являются цифрами\n')
    safe_input()


# Сортировка алгоритмом Хоара
def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)  # Выбираем число с которым будем сравнивать
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:  # Выбираем все элемены меньше выбранного и складываем в отдельный массив
                s_nums.append(n)
            elif n > q:  # Выбираем все элемены больше выбранного и складываем в отдельный массив
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)  # Возвращаем массив, составленный из трёх ранее созданных


# Начало выполнения программы согласно варианту
def start_program(matrix):
    listr = matrix
    print('Исходная матрица:')
    print(*listr, sep='\n')

    print()

    # Транспонируем матрицу
    listr = [[listr[w][q] for w in range(4)] for q in range(4)]
    print('Транспонированная матрица:')
    print(*listr, sep='\n')

    print()

    # Сортируем строки матрицы в правильном порядке, как по заданию
    listr = [quicksort(row) if q % 2 != 0 else
             quicksort(row)[::-1] for q, row in enumerate(listr)]
    print('Матрица после проведения сортировки по строкам:')
    print(*listr, sep='\n')

    print()

    # Транспонируем матрицу обратно
    listr = [[listr[w][q] for w in range(4)] for q in range(4)]
    print('Транспонированная обратно матрица(результат работы программы):')
    print(*listr, sep='\n')


# Запуск стартовой функции безопасного ввода
safe_input()
