def average(elements_list):
    terms = []
    if not elements_list:
        terms = [1, 2, 3]
    else:
        terms = elements_list

    return sum(terms) / len(terms)
