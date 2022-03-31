// Array data structure

class Array 
{
    int array[]=new int[5];
    public static  void main(String[] args) 
    {
        Array obj=new Array();
        for(int i=0; i<5;i++)
        {
            obj.array[i] = i;
        }
        for(int i=0; i<5;i++)
        {
            System.out.print(obj.array[i]+" ");
        }
    }
}