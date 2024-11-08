import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner

kivy.require('2.0.0')  # Ensure Kivy version is at least 2.0.0

# Functions for conversions
def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]

def binary_to_decimal(binary):
    return int(binary, 2)

def octal_to_decimal(octal):
    return int(octal, 8)

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_octal(decimal)

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_hexadecimal(decimal)

def octal_to_binary(octal):
    decimal = octal_to_decimal(octal)
    return decimal_to_binary(decimal)

def octal_to_hexadecimal(octal):
    decimal = octal_to_decimal(octal)
    return decimal_to_hexadecimal(decimal)

def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return decimal_to_binary(decimal)

def hexadecimal_to_octal(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return decimal_to_octal(decimal)

# GUI Class
class NumberSystemConverterApp(App):
    def build(self):
        self.title = 'Number System Converter'

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Label and Input Field
        self.input_label = Label(text="Enter the number:")
        self.number_input = TextInput(multiline=False, hint_text="Enter number", size_hint=(1, 0.1))
        layout.add_widget(self.input_label)
        layout.add_widget(self.number_input)

        # Spinner for number base
        self.base_spinner = Spinner(text='Select Base', values=('Binary', 'Decimal', 'Octal', 'Hexadecimal'), size_hint=(1, 0.1))
        layout.add_widget(self.base_spinner)

        # Button to perform conversion
        self.convert_button = Button(text="Convert", size_hint=(1, 0.1))
        self.convert_button.bind(on_press=self.convert_number)
        layout.add_widget(self.convert_button)

        # Results labels
        self.result_label = Label(text="Converted Results:")
        layout.add_widget(self.result_label)

        # Output labels for conversion results
        self.binary_label = Label(text="Binary: ")
        self.octal_label = Label(text="Octal: ")
        self.hexadecimal_label = Label(text="Hexadecimal: ")

        layout.add_widget(self.binary_label)
        layout.add_widget(self.octal_label)
        layout.add_widget(self.hexadecimal_label)

        return layout

    def convert_number(self, instance):
        # Get the input number and selected base
        number = self.number_input.text.strip()
        base = self.base_spinner.text

        try:
            # Depending on the base, convert to decimal
            if base == 'Binary':
                decimal_value = binary_to_decimal(number)
            elif base == 'Octal':
                decimal_value = octal_to_decimal(number)
            elif base == 'Hexadecimal':
                decimal_value = hexadecimal_to_decimal(number)
            else:
                decimal_value = int(number)  # Decimal input directly

            # Perform conversions
            binary_result = decimal_to_binary(decimal_value)
            octal_result = decimal_to_octal(decimal_value)
            hexadecimal_result = decimal_to_hexadecimal(decimal_value)

            # Display the results
            self.binary_label.text = f"Binary: {binary_result}"
            self.octal_label.text = f"Octal: {octal_result}"
            self.hexadecimal_label.text = f"Hexadecimal: {hexadecimal_result}"

        except ValueError:
            # Handle invalid input
            self.binary_label.text = "Binary: Invalid input"
            self.octal_label.text = "Octal: Invalid input"
            self.hexadecimal_label.text = "Hexadecimal: Invalid input"

# Run the application
if __name__ == '__main__':
    app = NumberSystemConverterApp()
    app.run()
