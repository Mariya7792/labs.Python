users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
users_dictionary = {"Общее количество": 0, "Уникальные посещения": 0}
users_dictionary["Общее количество"] = len(users)
users_dictionary["Уникальные посещения"] = len(set(users))
print(users_dictionary)
