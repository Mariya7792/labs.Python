def find_common_participants(participants1, participants2, separ=','):
    participants_first = set(participants1.split(separ))
    participants_second = participants2.split(separ)
    common = list(participants_first.intersection(participants_second))
    common_sort = sorted(common)

    return common_sort


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, '|')
print(participants)
