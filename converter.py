class Temperatura:
    def __init__(self, escala, temperatura):
        self.escala = escala
        self.temperatura = temperatura

class Conversor:
    def __init__(self, escala, temperatura):
        self.temp = Temperatura(escala, temperatura)
        print(f"Temperatura: {self.temp.temperatura:.2f} *{self.temp.escala}")

    def celsius_para_kelvin(self):
        temp_celsius = self.temp.temperatura
        temp_kelvin = temp_celsius + 273.0

        self.temp.escala = 'K'
        self.temp.temperatura = temp_kelvin
        print(f"Temperatura: {self.temp.temperatura:.2f} *{self.temp.escala}")

    def kelvin_para_celsius(self):
        temp_kelvin = self.temp.temperatura
        temp_celsius = temp_kelvin - 273.0

        self.temp.escala = 'C'
        self.temp.temperatura = temp_celsius
        print(f"Temperatura: {self.temp.temperatura:.2f} *{self.temp.escala}")

    def celsius_para_fahrenheit(self):
        temp_celsius = self.temp.temperatura
        temp_fahrenheit = (1.8 * temp_celsius) + 32.0

        self.temp.escala = 'F'
        self.temp.temperatura = temp_fahrenheit
        print(f"Temperatura: {self.temp.temperatura:.2f} *{self.temp.escala}")

    def fahrenheit_para_celsius(self):
        temp_fahrenheit = self.temp.temperatura
        temp_celsius = (temp_fahrenheit - 32.0) / 1.8

        self.temp.escala = 'C'
        self.temp.temperatura = temp_celsius
        print(f"Temperatura: {self.temp.temperatura:.2f} *{self.temp.escala}")

    def kelvin_para_fahrenheit(self):
        self.kelvin_para_celsius()
        self.celsius_para_fahrenheit()

    def fahrenheit_para_kelvin(self):
        self.fahrenheit_para_celsius()
        self.celsius_para_kelvin()

    def converter(self, escala_para_converter):
        print("Convertendo...")

        if escala_para_converter == 'C':
            if self.temp.escala == 'K':
                self.kelvin_para_celsius()
            elif self.temp.escala == 'F':
                self.fahrenheit_para_celsius()
        elif escala_para_converter == 'K':
            if self.temp.escala == 'C':
                self.celsius_para_kelvin()
            elif self.temp.escala == 'F':
                self.fahrenheit_para_kelvin()
        elif escala_para_converter == 'F':
            if self.temp.escala == 'C':
                self.celsius_para_fahrenheit()
            elif self.temp.escala == 'K':
                self.kelvin_para_fahrenheit()

if __name__ == '__main__':
    c = Conversor('K', 300)
    c.converter('F')
