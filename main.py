import task1_bubble_sort
import task2_calc_book_price

# Task 1:
# Вам дан код сортировки пузырьком, однако он работает неверно, там допущена ошибка.
# Используя дебагер, найдите и исправьте ошибку.
# Опишите в комментарии к коду, в чем была ошибка.
# Добавьте минимум 5 тестов для этого кода
print('Task 1: Fix bubble sort algorithm:')
task1_bubble_sort.print_bubble_sort_result()

# Task 2:
# Напишите программу на Python, которая на вход получает список списков
# и возвращает список кортежей. Каждый кортеж состоит из номера заказа и произведения цены на товары и
# количества. Стоимость товара должна быть увеличена на $10, если стоимость заказа меньше $100.
print('\nTask 2: Calculate price and add $10 for less than $100:')
task2_calc_book_price.print_calc_books_price()

# Task 3:
# Добавьте к исходному списку еще несколько товаров
print('\nTask 3: Add items to the list:')
task2_calc_book_price.print_list_with_added_elms()


# Task 4:
# Отсортируйте получившийся список по стоимости и выведите его на экран.
print('\nTask 4: Sort result list by price:')
task2_calc_book_price.print_sorted_by_price_list()

# Task 5:
# Используя filter() оставьте только книги, количество которых больше 5ти.
print('\nTask 5: Filtered list (quantity > 5):')
task2_calc_book_price.print_filtered_list()