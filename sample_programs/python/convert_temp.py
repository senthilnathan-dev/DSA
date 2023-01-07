# temperature conversion using python
# Fareinheit to celcius and vice versa


option = int(input("1.C to F\n2.F to C\nOPTION: "))

if option == 1:

    celcius = float(input("Enter celcius: "))
    farenheit = (celcius - 32) * (5/9) # logic
    print("Conversion result(in Farenheit): ",farenheit)

elif option == 2:

    farenheit = float(input("Enter farenheit: "))
    celcius = (farenheit * 9/5) + 32
    print("Conversion result(in Celcius): ", celcius)


# Contributed by Senthilnathan
