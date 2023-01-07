// C++ Program to convert celcius to farenheit and vice versa

#include <iostream>

// using the namespace directives
using std::cin;
using std::cout;
using std::endl;

int main()
{
    //  Declaration of variables
    float celcius, farenheit;
    int option;

    cout << "Enter your option\n1.Farenhit to Celcius\n2.Celcius to Farenhiet\nOPTION: ";
    cin >> option;

    if (option == 1)
    {
        cout << "Enter Farenhit: ";
        cin >> farenheit;

        celcius = (farenheit - 32) * (5.0 / 9.0); // test code
        // celcius = (farenheit - 32) * (5 / 9);
        cout <<  "The conversion result is(in Celcius): " << celcius << endl;
    }
    else if (option == 2)
    {
        cout << "Enter Celcius: ";
        cin >> celcius;

        farenheit = (celcius * 9 / 5) + 32;
        cout <<  "The conversion result is(in Farenheit): " << (float)farenheit << endl;
    }
    else
    {
        // Print incase of options other than 1,2.
        cout << "Invalid input!" << endl;
    }

    return 0;
}


// Contributed by Senthilnathan
