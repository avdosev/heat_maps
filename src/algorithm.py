def min_max(arg1, *args, key=lambda x: x):
    """
    :return: tuple(min_item, max_item)
    """
    # TODO fix to pythonic
    # arg1 — первый аргумент, args — список из второго и последующих аргументов
    if args:
        # Передали несколько аргументов — объединяем все в один список
        iterable = [arg1] + list(args)
    else:
        # Передали один аргумент — считаем, что он iterable
        iterable = arg1

    min_result = iterable[0]
    max_result = iterable[0]
    # Перебираем остальные элементы
    for item in iterable[1:]:
        key_item = key(item)
        if key_item > key(max_result):
            max_result = item
        if key_item < key(min_result):
            min_result = item

    return min_result, max_result
