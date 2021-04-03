class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def converter(cls, date: str):
        try:
            day, month, year = date.split('-')
            cls.validator(cls(day, month, year))
            return cls(day, month, year)
        except ValueError as e:
            print(e)

    @staticmethod
    def validator(obj):
        if 13 > int(obj.month) > 0 and len(obj.year) == 4 and 32 > int(obj.day) > 0:
            return True
        raise ValueError("Дата указана не верно!")


date = Data.converter('12-12-2020')
print(f"Дата: {date.day}.{date.month}.{date.year}\n")

data2 = Data.converter('123-12-2020')
