#temp = [10,50,60,100]
'''
import temperatur_calc

temperatur_calc.calc(L=[10,50,60,100])
print(temperatur_calc.calc)
'''

def get_temp():
    while True:
        C = input("Bitte gib einen Temp. in  Grad Celsius ein:")
        try: 
            C = float(C)
            return C
        except ValueError:
            print("Bitte gib eine gültige Temperatur ein.")

def convert_to_kelvin(C):
    K = C + 273.15
    return K

if __name__ == "__main__":
    C = get_temp()
    print("Das sind " + str(convert_to_kelvin(C)) + " Kelvin")




