def sort_by_score(users: list[dict], reverse=False):
    users_length = len(users)
    if users_length <= 1:
        return users

    for limit in range(users_length - 1, 0, -1):
        for index in range(limit):

            if not reverse:
                if users[index]['score'] < users[index + 1]['score']:
                    users[index], users[index + 1] = \
                        users[index + 1], users[index]

            if reverse:
                if users[index]['score'] > users[index + 1]['score']:
                    users[index], users[index + 1] = \
                        users[index + 1], users[index]

    return users
