books_list_initial = [
[34587, 'Learning Python, Mark Lutz', 4, 40.95],
[98762, 'Programming Python, Mark Lutz', 5, 56.80],
[77226, 'Head First Python, Paul Barry', 3, 32.95],
[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

books_list_to_add = [
[24387, ' на русском', 2, 4.59],
[18762, 'The C Programming Language (2nd Edition)', 12, 78.80],
[87236, 'C Programming Absolute Beginner\'s Guide', 1, 23.55],
[58132, 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14', 9, 42.89]
]


def calculate_books_price_map(books_list):
    result_list = list(map(lambda nested_elm:
                           (nested_elm[0], nested_elm[2]*nested_elm[3]
                           if nested_elm[2]*nested_elm[3] >=100
                           else (nested_elm[2]*nested_elm[3]+10)),
                           books_list))
    return result_list


def print_calc_books_price():
    result_list = calculate_books_price_map(books_list_initial)
    print_list_of_iterable(result_list)


def add_lists(list_initial, list_to_add):
    result_list = [y for x in [list_initial, list_to_add] for y in x]
    return result_list


def print_list_with_added_elms():
    result_list = add_lists(books_list_initial, books_list_to_add)
    print_list_of_iterable(result_list)


def sort_result_list_by_price(result_list):
    result_list.sort(key=lambda x: x[3])
    return result_list


def print_sorted_by_price_list():
    result_list = add_lists(books_list_initial, books_list_to_add)
    result_list_sorted = sort_result_list_by_price(result_list)
    print_list_of_iterable(result_list_sorted)


def filter_list_by_quantity(list_to_filter, quantity):
    return list(filter(lambda x: x[2] > quantity, list_to_filter))


def print_filtered_list():
    result_list = add_lists(books_list_initial, books_list_to_add)
    result_list_filtered = filter_list_by_quantity(list_to_filter=result_list, quantity=5)
    print_list_of_iterable(result_list_filtered)


def print_list_of_iterable(list_of_iterable):
    list(map(lambda x: print(x), list_of_iterable))


# def calculate_books_price(books_list):
#     result_list = list()
#     for book in books_list:
#         book_tuple_tmp = tuple(book)
#         id, name, quantity, price = book_tuple_tmp
#         order_price = quantity * price
#         if order_price < 100:
#             order_price += 10
#         result_tuple = (id, order_price)
#         result_list.append(result_tuple)
#     print(result_list)
