books_list_initial = [
[34587, 'Learning Python, Mark Lutz', 4, 40.95],
[98762, 'Programming Python, Mark Lutz', 5, 56.80],
[77226, 'Head First Python, Paul Barry', 3, 32.95],
[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


def calculate_books_price_map(books_list):
    result_list = list(map(lambda nested_elm:
                           (nested_elm[0], nested_elm[2]*nested_elm[3]
                           if nested_elm[2]*nested_elm[3] >=100
                           else (nested_elm[2]*nested_elm[3]+10)),
                           books_list))
    return result_list


def print_calc_books_price():
    print(calculate_books_price_map(books_list=books_list_initial))


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
