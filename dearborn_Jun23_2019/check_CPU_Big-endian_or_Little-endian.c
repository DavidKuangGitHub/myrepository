/*check_CPU_Big-endian_or_Little-endian.c 
Requirements: (1)Little and big endian are two ways of storing multibyte data-types ( int, float, etc). 
(2)In little endian machines, last byte of binary representation of the multibyte data-type is stored first. 
(3)On the other hand, in big endian machines, first byte of binary representation of the multibyte data-type is stored first.
Sample: Suppose that integer is stored as 4 bytes, if the variable x with value 0x12345670 , in Big-Endian, its 12then34then56then70 order0x100-0x101-0x102-0x103; 
however, in Little-Endian, its stored as 70then56then34then12 
Basically, memory is space/rooms like a line, everything that is stored into is placed via same order say 0x100then0x101then0x102then0x103 (In hex memory, you can say 1000then1001then1002then1003). Make sense?
If the most significant byte(s) is stored first, it's in Big-Endian format. Here the most significant a.k.a high/higher bits/bytes.
If the least significant byte(s) is stored first, it's in Little-Endian format. Here the least significant a.k.a low/lower bits/bytes.  


*/
#include <stdio.h>

int main()
{
        printf("To run this c script to check whether current CPU is Big-endian or Little-endian ...\n");
        int i =1; 
        char *p = (char *) &i; 
        if (*p == 1)
            printf("It is Little Endian");
        else 
            printf("It is Big Endian");
}
