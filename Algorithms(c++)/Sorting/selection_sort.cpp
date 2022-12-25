// selection sort
// Time Complexity O(N^2)

#include <iostream>

using namespace std;

// declaration
void swap(int *a, int *b);
void selection(int *arr, int size);
void display(int *arr, int size);

// definition
void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void selection(int *arr, int size)
{
    for(int i = 0; i < size; i++)
    {
        int l_index = i;
        for(int j = i+1; j < size; j++)
        {
            if (arr[j] < arr[l_index])
            {
                l_index = j;
            }
        }
        swap(&arr[i], &arr[l_index]);
    }
}

void display(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main()
{
    int arr[7] = {55, 10, 12, 89, 51, 20, 11};
    int size = sizeof(arr)/sizeof(int);
    cout << "Before sorting" << endl;
    display(&arr[0], size);
    cout << "After sorting" << endl;
    selection(&arr[0], size);
    display(&arr[0], size);
    
    return 0;
}
