class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"Дата: {date.day}.{date.month}.{date.year}\n"

    @classmethod
    def converter(cls, data: str):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            cls.validator(cls(day, month, year))
            return cls(day, month, year)
        except ValueError as e:
            print(e)

    @staticmethod
    def validator(obj):
        if 13 > obj.month > 0 and 2022 > obj.year > 0 and 32 > obj.day > 0:
            return True
        raise ValueError("Дата указана не верно!")


date = Data.converter('12-12-2020')
print(date)

date2 = Data.converter('123-12-2020')
print(date2)
