rates = {
    "KGS": 1,
    "USD": 87.55,
    "EUR": 98,
    "RUB": 1.055
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    def convert_to_kgs(self):
        return self.amount * rates[self.currency]

    def __add__(self, other):
        t = self.convert_to_kgs() + other.convert_to_kgs()
        return Money(t, "KGS")
    def __sub__(self, other):
        t = self.convert_to_kgs() - other.convert_to_kgs()
        return Money(t, "KGS")
    def __mul__(self, other):
        return Money(self.amount * other, self.currency)
    def __truediv__(self, other):
        return Money(self.amount / other, self.currency)
    def __str__(self):
        return f"{self.amount} {self.currency}"

money1 = Money(100, "USD")
money2 = Money(5000, "KGS")

result1 = money1 + money2
result2 = money1 - money2
result3 = money1 * 3
result4 = money1 / 2

print("SUM:", result1)
print("SUB:", result2)
print("MUL:", result3)
print("DIV:", result4)