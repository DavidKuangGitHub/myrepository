#include <stdio.h>
#include <time.h>

int main(void){
	struct tm* ptr;
	time_t lt;
	lt= time(NULL);
	/*ptr = localtime(<);*/
	/*ptr = localtime(&l&ltt);*/
	ptr = gmtime(&lt);  /*This is t get UTC time Coordinated Universal Tim  */
	printf("UTC time is %s",asctime(ptr));
	return 0;
}

