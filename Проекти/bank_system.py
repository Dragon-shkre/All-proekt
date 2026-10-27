class BankAccount:

    def __init__(self, owner_name, account_number, balance):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Пополнение: +{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Снято: -{amount}")
        else:
            print("Недостаточно средств!")

    def show_balance(self):
        print("Баланс: ", self.balance)

    def show_history(self):
        for operation in self.history:
            print(operation)

    def transfer(self, other_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount

            self.history.append(f"Перевод: -{amount}")
            other_account.history.append(f"Перевод: +{amount}")
        else:
            print("Недостаточно денег!")
accounts = []
def create_account():
    name = input("Имя владельца: ")
    number = input("Номер счёта: ")
    balance = float(input("Начальный баланс:"))

    account = BankAccount(name, number, balance)
    accounts.append(account)

def show_account():
    for account in accounts:
        print("=" * 30)
        print("Владелец:", account.owner_name)
        print("Номер счёта:", account.account_number)
        print("Баланс:", account.balance)
        print("=" * 30)

def find_account():
    number = input("Введите номер счёта: ")
    for account in accounts:
        if number == account.account_number:
            print(account.owner_name)
            print(account.account_number)
            print(account.balance)
            return
    else:
        print("Счёт не найден!")

def deposit_to_account():
    number = float(input("Введите номер счёта: "))
    for account in accounts:
        if number == account.account_number:
            amount = float(input("Сумма пополнения: "))
            account.deposit(amount)
            print("Счёт успешно пополнен!")
            return

        print("Счёт не найден!")

def withdraw_from_account():
    number = input("Введите номер счёта: ")

    for account in accounts:
        if number == account.account_number:
            amount =float(input("Сумма снятия:"))
            account.withdraw(amount)
            return

    print("Счёт не найден!")

def transfer_money():
    sender_number = input("Номер счёта отправителя: ")
    receiver_number = input("Номер счёта получателя: ")

    sender = None
    receiver = None

    for account in accounts:
        if account.account_number == sender_number:
            sender = account

        if account.account_number == receiver_number:
            receiver = account

    if sender is None:
        print("Счёт отправителя не найден!")
        return

    if receiver is None:
        print("Счёт получателя не найден!")
        return

    amount = float(input("Сумма перевода: "))

    sender.transfer(receiver, amount)

def show_history():
    number = input("Введите номер счёта: ")

    for account in accounts:
        if account.account_number == number:
            account.show_history()
            return

    print("Счёт не найден!")


def show_menu():
    print("=" * 30)
    print("      БАНКОВСКАЯ СИСТЕМА")
    print("=" * 30)
    print("1. Создать счёт")
    print("2. Показать все счета")
    print("3. Найти счёт")
    print("4. Пополнить счёт")
    print("5. Снять деньги")
    print("6. Перевести деньги")
    print("7. История операций")
    print("8. Выход")
    print("=" * 30)


while True:
    show_menu()

    choice = input("Выберите пункт: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        show_accounts()

    elif choice == "3":
        find_account()

    elif choice == "4":
        deposit_to_account()

    elif choice == "5":
        withdraw_from_account()

    elif choice == "6":
        transfer_money()

    elif choice == "7":
        show_history()

    elif choice == "8":
        print("До свидания!")
        break

    else:
        print("Неверный выбор!")