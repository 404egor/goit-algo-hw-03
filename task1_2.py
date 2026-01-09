import random

try:
    min = int(input("Введіть число >=1"))
    max = int(input("Введіть число <=1000"))
    quantity = int(input("Введіть кількість чисел"))
except ValueError:
    print("Помилка даних")

def get_numbers_ticket(min, max, quantity):
    try:  
        list_number = set()

        if min >= 1 and max <=1000 and quantity <= max-min+1:
            while len(list_number) != quantity:
                list_number.add(random.randint(min, max))
        else:
            return []
        result = list(list_number)
    except ValueError:
        print("Помилка даних")

    return sorted(result)
        
print(get_numbers_ticket(min, max, quantity))


