import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.datetime.now().date()
        today_spent = 0
        for record in self.records:
            if record.date == today:
                today_spent += record.amount
        return today_spent

    def get_week_stats(self):
        today = dt.datetime.now().date() # дата сегодня
        week_ago = today - dt.timedelta(7) # дата того дня, с которого берется отсчет последних семи дней
        week_spent = 0
        for record in self.records:
            if record.date >= week_ago and record.date <= today:
                week_spent += record.amount
        return week_spent
                

class Record:
    def __init__(self, amount, comment, date = dt.datetime.now().date()):
        self.amount = amount
        self.comment = comment
        if date != dt.datetime.now().date(): # если необязательный параметр date был передан в аргументах экземпляра
            date_format = '%d.%m.%Y'
            moment = dt.datetime.strptime(date, date_format) # приводим дату к формату '%Y.%m.%d'
            self.date = moment.date() 
        else:
            self.date = date


class CashCalculator(Calculator):
    USD_RATE = 73.72
    EURO_RATE = 89.33

    def get_today_cash_remained(self, currency: str):
        balance = self.limit - self.get_today_stats() # текущий остаток денег на сегодня
        if currency == 'rub':
            abs_balance = abs(balance) # баланс по модулю
            currency_txt = 'руб'
        elif currency == "eur":
            abs_balance = round(abs(balance) / self.EURO_RATE, 2) # баланс по 
            currency_txt = 'Euro' # модулю переводим в евро оставляя два знака после запятой
        else:
            abs_balance = round(abs(balance) / self.USD_RATE, 2) # то же самое в доллары
            currency_txt = 'USD'
        if balance > 0:
            return f'На сегодня осталось {abs_balance} {currency_txt}'
        elif balance == 0:
            return 'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {abs_balance} {currency_txt}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        balance = self.limit - self.get_today_stats()
        if balance > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {balance} кКал'
        else:
            return 'Хватит есть!'