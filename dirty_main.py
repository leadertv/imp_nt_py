import datetime
from application.salary import *
from application.db.people import *


def main():
    print(f"Текущая дата и время: {datetime.datetime.now()}")
    calculate_salary()
    get_employees()


if __name__ == '__main__':
    main()
