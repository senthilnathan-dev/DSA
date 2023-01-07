// Java implementaion of temperature conversion

import java.util.Scanner;

class ConvertTemp
{
    public static void main(String arg[])
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your option: ");
        int opt = sc.nextInt();

        switch(opt)
        {


        case 1 :
        {

            System.out.print("Enter your Celcius: ");

            float Celcius = sc.nextFloat();
            float Farenheit = (Celcius - 32) * 5 / 9;

            System.out.print(Farenheit);

            break;
        }

        case 2 :
        {

            System.out.print("Enter your Farenheit: ");

            float Farenheit = sc.nextFloat();
            float Celcius = (Farenheit * 9/5 )  + 32;

            System.out.print(Celcius);
            break;
        }

        default :
        {
            System.out.print("Enter valid option");
        }
    }
    }
}


//  Contributed by Ramachandran
