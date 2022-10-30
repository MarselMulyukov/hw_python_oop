import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def today_remained(self):
        return self.limit - self.get_today_stats()

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.datetime.now().date()
        list_of_spendings = [record.amount for record in self.records if
                             record.date == today]
        return sum(list_of_spendings)

    def get_week_stats(self):
        today = dt.datetime.now().date()  # дата сегодня
        week_ago = today - dt.timedelta(7)  # дата неделю назад
        list_of_spendings = [record.amount for record in self.records if
                             week_ago < record.date <= today]
        return sum(list_of_spendings)


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date:
            date_format = '%d.%m.%Y'
            moment = dt.datetime.strptime(date, date_format)
        else:
            moment = dt.datetime.now()
        self.date = moment.date()


class CashCalculator(Calculator):
    USD_RATE = 73.72
    EURO_RATE = 89.33

    def get_today_cash_remained(self, currency: str):
        currencies_dict = {'rub': (1, 'руб'), 'eur': (self.EURO_RATE, 'Euro'),
                           'usd': (self.USD_RATE, 'USD')}
        balance = self.today_remained()
        abs_balance = abs(balance)
        rate, currency_txt = currencies_dict[currency]
        recounted = round(abs_balance / rate, 2)
        if balance > 0:
            return (f'На сегодня осталось {recounted}'
                    f' {currency_txt}')
        elif balance == 0:
            return 'Денег нет, держись'
        return (f'Денег нет, держись: твой долг - {recounted}'
                f' {currency_txt}')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        balance = self.today_remained()
        if balance > 0:
            return ('Сегодня можно съесть что-нибудь ещё, но с общей'
                    f' калорийностью не более {balance} кКал')
        return 'Хватит есть!'
