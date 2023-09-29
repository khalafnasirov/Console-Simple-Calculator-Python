class Calculator:
    def __init__(self) -> None:
        print("Calculater app started")

        self.first_num = 0
        self.second_num = 0
        self.result = 0

    def get_operands(self):
        while True:
            self.first_num = input("Enter first operand: ")
            if self.first_num.isdigit():
                self.first_num = int(self.first_num)
                break
            else:
                print("Please enter number")
        while True:
            self.second_num = input("Enter second operand: ")
            if self.second_num.isdigit():
                self.second_num = int(self.second_num)
                break
            else:
                print("Please enter number")
    
    def select_operator(self):
        print("Select any operations below:")
        print('''
              1. Addition
              2. Subtraction
              3. Multiplaction
              4. Division
              ''')
        while True:
            operator_num = input("Enter selection number: ")
            if operator_num.isdigit():
                operator_num = int(operator_num)
                if operator_num not in [1,2,3,4]:
                    print("Enter valid selection number")
                else: 
                    self.do_operation(operator_num)
                    break
            else:
                print("Enter number")
                
                        

    def do_operation(self,number):
        def show_process(message):
            print(f"{message} {self.first_num} and {self.second_num}")
        match number:
            case 1:
                show_process("Adding")
                self.result = self.first_num + self.second_num
            case 2:
                show_process("Subtracting")
                self.result = self.first_num - self.second_num

            case 3:
                show_process("Multiplying")
                self.result = self.first_num * self.second_num

            case 4:
                show_process("Dividing")
                if (self.second_num != 0):
                    self.result = self.first_num + self.second_num
                else:
                    print("Process failed, because you can't divide by zero")
    
    def show_answer(self):
        print(f"Result is: {self.result}")

if __name__ == "__main__":
    calc = Calculator()
    calc.get_operands()
    calc.select_operator()
    calc.show_answer()
