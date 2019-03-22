import tkinter as Tk
import math


class Calculator:

    def __init__(self, parent):

        self.operations = {'+': False,
                           '-': False,
                           '*': False,
                           '/': False}
        self.first_number_selected = 0

        self.second_number_selected = 0

        expand_button = Tk.N + Tk.E + Tk.S + Tk.W

        self.display_label = Tk.Label(parent, text='0', font='Verdana 16 bold',
                                      bg='white', fg='black', height=2, width=4)
        self.display_label.grid(row=0, column=0, columnspan=4, sticky=expand_button)

        Tk.Button(parent, text='0', command=self._number_callback(0)).grid(row=4, columnspan=2, sticky=expand_button)
        for number in range(1, 10):
            callback = self._number_callback(number)
            row = math.ceil(number/3)
            col = (number-1) % 3
            Tk.Button(parent, text=str(number), height=2, width=6, command=callback).grid(row=row, column=col)

        for position, operator in enumerate(self.operations.keys()):
            Tk.Button(parent, text=operator, height=2, width=6,
                      command=self._operation_callback(operator)).grid(row=position + 1, column=3)
        Tk.Button(parent, text='C', height=2, width=6, command=self.reset).grid(row=4, column=2)
        Tk.Button(parent, text='=', height=2, command=self.calculate_result).grid(row=5, columnspan=4, sticky=expand_button)

    def number_pressed(self, button_number):

        if not any(self.operations.values()):
            if self.first_number_selected == 0:
                self.first_number_selected = button_number
                self.display_label['text'] = str(button_number)
            else:
                self.display_label['text'] += str(button_number)
                self.first_number_selected = int(self.display_label['text'])
        elif self.second_number_selected == 0:
            self.second_number_selected = button_number
            self.display_label['text'] = str(button_number)
        else:
            self.display_label['text'] += str(button_number)
            self.second_number_selected = int(self.display_label['text'])

    def _number_callback(self, number):

        return lambda: self.number_pressed(number)

    def operation_selected(self, operation):

        if self.second_number_selected and self.first_number_selected:
            self.first_number_selected = self.calculate_result()
            self.display_label['text'] = str(self.first_number_selected)

        self._reset_operations()
        self.operations[operation] = True

    def _operation_callback(self, sign):

        return lambda: self.operation_selected(sign)

    def _reset_operations(self):

        for operator in self.operations.keys():
            self.operations[operator] = False

    def calculate_result(self):

        result = self.first_number_selected

        # create dictionary for operations so i can add more

        if self.operations['+']:
            result = self.first_number_selected + self.second_number_selected
        elif self.operations['-']:
            result = self.first_number_selected - self.second_number_selected
        elif self.operations['*']:
            result = self.first_number_selected * self.second_number_selected
        elif self.operations['/']:
            result = round(self.first_number_selected / self.second_number_selected, 3)
            result = int(result) if result.is_integer() else result

        self.first_number_selected = result
        self.second_number_selected = 0
        self._reset_operations()
        self.display_label['text'] = str(result)
        return result

    def reset(self):
        """Reset all the variables to their default states"""
        self.first_number_selected = 0
        self.second_number_selected = 0
        self._reset_operations()
        self.display_label['text'] = '0'


    def run():
        frame = Tk.Tk()
        frame.wm_title('Calculator')
        frame.resizable(width=False, height=False)
        Calculator(frame)
        frame.mainloop()


def main():
    Calculator.run()


if __name__ == '__main__':
    main()














