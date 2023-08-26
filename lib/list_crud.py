def create_an_empty_list():
    return []


def create_a_list():
    new_list = ["Great", "wash", "b", "eat"]
    return new_list

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l


def remove_element_from_end_of_list(l):
    if len(l) > 0:
        l.pop()
    return l
def remove_element_from_start_of_list(l):
    if len(l) > 0:
        del l[0]
        return l


def retrieve_first_element_from_list(l):
    if len(l) > 0:
        first_number = l[0]
        return first_number
    else:
        return None


def retrieve_element_from_index(l, index):
    number_retrieved = l[index]
    return number_retrieved


def retrieve_last_element_from_list(l):
    last_element = l[-1]
    return last_element
