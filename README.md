## Lesson02Seminar01HW

1. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

2. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

3. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

4. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

5. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
*Пример:* <br>
6 -> да <br>
7 -> да <br>
1 -> нет <br>

7. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

8. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).<br>
Пример:<br>
x = 34, y = -30 -> 4 <br>
x = 2, y = 4 -> 1 <br>
x = -34, y = -30 -> 3 <br>

9. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

10. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. <br>
Пример: <br>
A (3,6); B (2,1) -> 5,09 <br>
A (7,-5); B (1,-1) -> 7,21 <br>

___

## Lesson03Seminar02HW

1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

2. Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.<br>
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2. <br>
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2. <br>
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2. <br>
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1. <br>
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя. <br>
Пример готовой структуры: <br>
[<br>
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),<br>
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),<br>
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})<br>
]<br>
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.<br>
Пример:<br>
{<br>
“название”: [“компьютер”, “принтер”, “сканер”],<br>
“цена”: [20000, 6000, 2000],<br>
“количество”: [5, 2, 7],<br>
“ед”: [“шт.”]<br>
}<br>

7. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Пример: <br>
6782 -> 23 <br>
0,56 -> 11 <br>

8. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. <br> 
Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

9. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.<br>
Пример:<br>
Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}<br>

10. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

11. Реализуйте алгоритм перемешивания списка.

___

## Lesson05Seminar03HW

1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень. <br>
Подсказка: попробуйте решить задачу двумя способами. <br>
Первый — возведение в степень с помощью оператора **. <br>
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.<br>
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

7. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции. <br>
Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

8. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример: <br>
[2, 3, 4, 5, 6] => [12, 15, 16] <br>
[2, 3, 5, 6] => [12, 15] <br>

9. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. <br>
Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

10. Напишите программу, которая будет преобразовывать десятичное число в двоичное. <br>
Пример:<br>
45 -> 101101 <br>
3 -> 11 <br>
2 -> 10 <br>

11. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.<br>
Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

___

## Lesson06Seminar04HW

1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.<br>
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.<br>
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].<br>
Результат: [12, 44, 4, 10, 78, 123].

3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку. <br>
Подсказка: использовать функцию range() и генератор.

4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.<br>
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].<br>
Результат: [23, 1, 3, 10, 4, 11]<br>

5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.<br>
Подсказка: использовать функцию reduce().

6. Реализовать два небольших скрипта:<br>
а) итератор, генерирующий целые числа, начиная с указанного; <br>
б) итератор, повторяющий элементы некоторого списка, определенного заранее.<br>
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.<br>
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.<br>
Подсказка: факториал числа n — произведение чисел от 1 до n.<br>
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

8. Вычислить число c заданной точностью d $(10^{-1} ≤ d ≤10^{-10})$<br>
Пример: при $d = 0.001, π = 3.141$<br>

9. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

10. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

11. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.<br>
Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

12. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

___

## Lesson08Seminar05HW

1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников. <br>
Пример файла: <br>
Иванов 23543.12 <br>
Петров 13749.32 <br>

4. Создать (не программно) текстовый файл со следующим содержимым:<br>
One — 1<br>
Two — 2<br>
Three — 3<br>
Four — 4<br>
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

___

## Lesson09Seminar06HW

1. Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени, оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться.

2. Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти, оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться.

Описания нужно делать в виде docstrings.

___

## Lesson11Seminar07HW

1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т

3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

___

## Lesson12Seminar08HW

1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.<br>
[[], [], []]<br>
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.<br>
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

2. Реализовать программу работы с органическими клетками, состоящими из ячеек.<br>
Необходимо создать класс Клетка (Cell).<br>
В его конструкторе инициализировать параметр (quantity), соответствующий количеству ячеек клетки (целое число).<br>
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()),<br>
вычитание (sub()),<br>
умножение (mul()),<br>
деление (truediv()).<br>
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.<br>
Сложение. Объединение двух клеток.<br>
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.<br>
Вычитание. Участвуют две клетки.<br>
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.<br>
Умножение. Создается общая клетка из двух.<br>
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.<br>
Деление. Создается общая клетка из двух.<br>
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.<br>

3. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

___

## Lesson14Seminar09HW

Написать тесты для ДЗ уроков 1-8:
* не менее 10 тестов
* желательно с разными ф-циями (assertEqual, assertRaises и т.д.)
* тесты не должны быть вместе с исходным кодом (нужно разместить в разных модулях)

___

## Lesson15Seminar10HW

1. Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ

2. Создать метакласс для паттерна Синглтон

___

## Lesson17Seminar11HW

1. Каждое из слов «разработка», «сокет», «декоратор» представить в буквенном формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать в набор кодовых точек
Unicode (НО НЕ В БАЙТЫ!!!) и также проверить тип и содержимое переменных.<br>
Подсказки:
   - 'разработка' - буквенный формат
   - '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
   - используйте списки и циклы, не дублируйте функции


2. Каждое из слов «class», «function», «method» записать в байтовом формате без преобразования в последовательность 
кодов не используя!!! методы encode и decode) и определить тип, содержимое и длину соответствующих переменных. <br>
Подсказки:
   - b'class' - используйте маркировку b''
   - используйте списки и циклы, не дублируйте функции


3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе с помощью 
маркировки b'' (без encode decode). <br>
Подсказки:
   - используйте списки и циклы, не дублируйте функции
   - обязательно!!! усложните задачу, "отловив" и обработав исключение, придумайте как это сделать


4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое 
и выполнить обратное преобразование (используя методы encode и decode). <br>
Подсказки:
   - используйте списки и циклы, не дублируйте функции


5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
   - используйте модуль chardet


6. Создать  НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». <br>
Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Это значит, что при чтении файла вы должны явно указать кодировку utf-8 
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта. <br>
Подсказки:
   - обратите внимание, что заполнять файл вы можете в любой кодировке но открыть нужно в формате Unicode (utf-8)
   - обратите внимание на чтение файла в режиме rb для последующей переконвертации в нужную кодировку
