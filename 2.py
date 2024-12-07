# TODO Напишите функцию find_common_participants
def find_common_participants(participants1, participants2, separator=","):

    participants1 = participants1.split(separator)
    participants2 = participants2.split(separator)

    common_participants = set(participants1).intersection(participants2)

    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)