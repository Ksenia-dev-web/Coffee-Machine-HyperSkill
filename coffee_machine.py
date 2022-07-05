class CoffeeMachine:
      def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
            self.water = water
            self.milk = milk
            self.beans = beans
            self.cups = cups
            self.money = money

      def actions(self):
            while True:
                  action = input('Write action (buy, fill, take, remaining, exit):')
                  if action == 'buy':
                        self.buy()
                  elif action == 'fill':
                        self.fill()
                  elif action == 'take':
                        self.take()
                  elif action == 'remaining':
                        self.remaining()
                  elif action == 'exit':
                        break

      def make_espresso(self):
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4

      def make_latte(self):
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7

      def make_cappuccino(self):
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6

      def buy(self):
            coffee = input('What do you want to buy& 1 - espresso, 2 - latte, 3 - cappuccino:')
            if coffee == '1':
                  if self.water < 250:
                        print('Sorry, not enough water!')
                  elif self.beans < 16:
                        print('Sorry, not enough coffee beans!')
                  elif self.cups < 1:
                        print('Sorry, not enough disposable cups!')
                  else:
                        print('I have enough resources, making your coffee!')
                        self.make_espresso()
            elif coffee == '2':
                  if self.water < 350:
                        print('Sorry, not enough water!')
                  elif self.milk < 75:
                        print('Sorry, not enough milk!')
                  elif self.beans < 20:
                        print('Sorry, not enough coffee beans!')
                  elif self.cups < 1:
                        print('Sorry, not enough disposable cups!')
                  else:
                        print('I have enough resources, making your coffee!')
                        self.make_latte()
            elif coffee == '3':
                  if self.water < 200:
                        print('Sorry, not enough water!')
                  elif self.milk < 100:
                        print('Sorry, not enough milk!')
                  elif self.beans < 12:
                        print('Sorry, not enough coffee beans!')
                  elif self.cups < 1:
                        print('Sorry, not enough disposable cups!')
                  else:
                        print('I have enough resources, making your coffee!')
                        self.make_cappuccino()
            elif coffee == 'back':
                  print('')
            else:
                  self.buy()

      def fill(self):
            print('Write how many ml of water you want to add:')
            self.water += int(input())
            print('Write how many ml of milk you want to add:')
            self.milk += int(input())
            print('Write how many grams of coffee beans you want to add:')
            self.beans += int(input())
            print('Write how many disposable cups you want to add:')
            self.cups += int(input())

      def take(self):
            print(f'I gave you ${self.money}')
            self.money = 0

      def remaining(self):
            print(f'The coffee machine has:\n'
                  f'{self.water} ml of water\n'
                  f'{self.milk} ml of milk\n'
                  f'{self.beans} g of coffee beans\n'
                  f'{self.cups} disposable cups\n'
                  f'${self.money} of money')



coffee_machine = CoffeeMachine()
coffee_machine.actions()

# another solution with funcs only
# espresso = [250, 0, 16, 4, 1]
# latte = [350, 75, 20, 7, 1]
# cappuccino = [200, 100, 12, 6, 1]
# initial_values = [400, 540, 120, 550, 9]
#
# def action():
#       choice = input('Write action (buy, fill, take):')
#       if choice == 'buy':
#             buy()
#       elif choice == 'fill':
#             fill()
#       elif choice == 'take':
#             take()
#
#
# def buy():
#       choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
#       if choice == '1':
#             information_print(espresso[0], espresso[1], espresso[2], espresso[3], espresso[4])
#       elif choice == '2':
#             information_print(latte[0], latte[1], latte[2], latte[3], latte[4])
#       elif choice == '3':
#             information_print(cappuccino[0], cappuccino[1], cappuccino[2], cappuccino[3], cappuccino[4])
#
#
# def information_print(a, b, c, d, e):
#       print("The coffee machine has:")
#       print(f"{initial_values[0] - a} ml of water")
#       print(f"{initial_values[1] - b} ml of milk")
#       print(f"{initial_values[2] - c} g of coffee beans")
#       print(f"{initial_values[4] - e} disposable cups")
#       print(f"${initial_values[3] + d} of money")
#
#
# def fill():
#     print("Write how many ml of water you want to add:")
#     add_water = int(input(""))
#     print("Write how many ml of milk you want to add:")
#     add_milk = int(input(""))
#     print("Write how many grams of coffee beans you want to add:")
#     add_coffee = int(input(""))
#     print("Write how many disposable cups you want to add:")
#     add_cups = int(input(""))
#     print()
#     information_print(-add_water, -add_milk, -add_coffee, 0, -add_cups)
#
#
# def take():
#     print(f"I gave you ${initial_values[3]}")
#     print()
#     information_print(0, 0, 0, -initial_values[3], 0)
#
#
# def main():
#     information_print(0, 0, 0, 0, 0)
#     print()
#     action()
#
#
# if __name__ == '__main__':
#     main()