class Error:
    def error(self):
        return "Помилка"

class Success:
    def success(self):
        return "Успіх"

class Fifteen(Success):
    pass

class Thirty_five(Error, Success):
    pass

class Fifty(Error):
    pass

class Thirty(Error):
    pass

class Ten(Fifteen):
    pass

class Twenty_five(Fifty, Thirty):
    pass

class Five(Thirty_five, Ten):
    pass

class Begin(Five, Twenty_five):
    pass

begin_instance = Begin()
thirty_five_instance = Thirty_five()

print(begin_instance.error())
print(thirty_five_instance.success())
