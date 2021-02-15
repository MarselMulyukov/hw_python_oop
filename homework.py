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
        '''Здесь тоже использовал List comprehensions'''
        today = dt.datetime.now().date()
        list_of_spendings = [record.amount for record in self.records if
                             record.date == today]
        return sum(list_of_spendings)

    def get_week_stats(self):
        '''Берем даты большие или равные первому дню последних семи дней'''
        today = dt.datetime.now().date()  # дата сегодня
        week_ago = today - dt.timedelta(6)  # первый из последних семи дней
        list_of_spendings = [record.amount for record in self.records if
                             week_ago <= record.date <= today]
        return sum(list_of_spendings)


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date:  # если необязательный параметр
            date_format = '%d.%m.%Y'  # date передан в аргументах экземпляра
            moment = dt.datetime.strptime(date, date_format)  # приводим дату
            self.date = moment.date()  # к формату '%Y.%m.%d'
        else:
            self.date = dt.datetime.now().date()


class CashCalculator(Calculator):
    USD_RATE = 73.72
    EURO_RATE = 89.33

    def get_today_cash_remained(self, currency: str):
        '''Здесь использовал тоже return без else. Не доволен количеством
        задействуемых переменных. Может быть что-то подскажешь?'''
        currencies_dict = {'rub': (1, 'руб'), 'eur': (self.EURO_RATE, 'Euro'),
                           'usd': (self.USD_RATE, 'USD')}
        balance = self.today_remained()
        abs_balance = abs(balance)
        recounted = round(abs_balance / currencies_dict[currency][0], 2)
        currency_txt = currencies_dict[currency][1]
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
