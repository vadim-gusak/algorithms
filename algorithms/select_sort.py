def sort_by_score(users: list[dict], reverse=False) -> list:
    users_len = len(users)
    if users_len <= 1:
        return users

    for index_1 in range(users_len - 1):
        for index_2 in range(index_1 + 1, users_len):

            if not reverse and \
                    users[index_2]['score'] > users[index_1]['score']:
                users[index_1], users[index_2] = \
                    users[index_2], users[index_1]

            if reverse and \
                    users[index_2]['score'] < users[index_1]['score']:
                users[index_1], users[index_2] = \
                    users[index_2], users[index_1]

    return users
