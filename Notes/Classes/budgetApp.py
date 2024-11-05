class Category:
    def __init__(self, category):
        self.category = category
        self.balance = 0
        self.spend = 0
        self.ledger = []

    def __str__(self):
        category_str = ''
        # Make tittle
        x = (30 - len(self.category)) // 2
        y = 30 - x - len(self.category)
        category_str = '*' * x + self.category + '*' * y + '\n'
        for dict in self.ledger:
            description_str = ''
            amount_str = ''
            # Max description length: 23
            counter = 0
            for char in dict['description']:
                counter +=1
                description_str += char
                if counter == 23:
                    break
            # Max amount length: 7
            counter = 0
            for digit in "{:.2f}".format(float(dict['amount'])):
                counter +=1
                amount_str += digit
                if counter == 7:
                    break
            spaces = 30 - len(description_str) - len(amount_str)
            category_str += description_str + ' ' * spaces + amount_str + '\n'
        category_str += f'Total: {self.balance}'
        return category_str

    def deposit(self, amount, description = ''):
        # Should I check if amount is positive?
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})
        
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.balance -= amount
            self.spend += amount
            self.ledger.append({'amount': - amount, 'description': description})
        return self.check_funds(amount)

    def get_balance(self):
        return self.balance

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination.category}')
            destination.deposit(amount, f'Transfer from {self.category}')
        return self.check_funds(amount)

    def check_funds(self, amount):
        return self.balance >= amount

def create_spend_chart(categories):
    spend_chart = 'Percentage spent by category\n'
    # Computing the total spendses
    relative_spendses = []
    total_spend = 0
    names = []
    names_len = []
    for category in categories:
        total_spend += category.spend
        names.append(category.category)
        names_len.append(len(category.category))
    # Computing relative spendses
    for category in categories:
        relative_spendses.append(category.spend/total_spend * 100)

    for n in range(100,-10,-10):
        spend_chart += ' ' * (3 - len(str(n))) + str(n) + '|' + ' '
        for spend in relative_spendses:
            if spend >= n:
                spend_chart += 'o' + ' ' * 2
            else: 
                spend_chart += ' ' * 3
        spend_chart += '\n'
    spend_chart += ' ' * 4 + '-' * (3 * len(categories) + 1) + '\n'    

    for i in range(max(names_len)):
        spend_chart += ' ' * 5
        for j in range(len(names)):
            if i < len(names[j]):
                spend_chart += names[j][i] + ' ' * 2
            else:
                spend_chart += ' ' * 3
        if i != max(names_len) - 1:
            spend_chart += '\n'

    return spend_chart

food = Category('Food')
food.deposit(1000)
food.withdraw(450)
drugs = Category('Drugs')
drugs.deposit(1000)
drugs.withdraw(50)

print(create_spend_chart([food,drugs]))

print('El programa se ejecuto correctamente.')