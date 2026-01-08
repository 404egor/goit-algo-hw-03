import datetime 

def get_days_from_today(users_input):
    try:
        users_date = datetime.datetime.strptime(users_input, "%Y-%m-%d").date()
        date_now = datetime.datetime.today().date()

        return (date_now - users_date).days
    except ValueError:
        return "Неправильний формат. Використовуйте YYYY-MM-DD"
    
users_input = input("Напишіть дату у вигляді: '%Y-%m-%d'")
print(get_days_from_today(users_input))