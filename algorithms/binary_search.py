def search(phonebook: list[dict], name: str) -> str:
    phonebook_length = len(phonebook)

    if phonebook_length == 0:
        return 'Phonebook is empty!'

    first = 0
    last = phonebook_length - 1
    middle = last // 2

    while first <= last:

        if phonebook[middle]['name'] == name:
            return phonebook[middle]['number']

        if phonebook[middle]['name'] > name:
            last = middle - 1

        if phonebook[middle]['name'] < name:
            first = middle + 1

        middle = (first + last) // 2

    return 'Name not found!'
