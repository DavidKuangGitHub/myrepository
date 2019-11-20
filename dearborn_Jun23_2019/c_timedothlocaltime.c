#include <stdio.h>
#include <time.h>

int main(void){
	struct tm* ptr;
	time_t lt;
	lt= time(NULL);
	ptr = localtime(&lt);/* To get local time  */
	printf("Localtime =  %s",asctime(ptr));
	return 0;
}

