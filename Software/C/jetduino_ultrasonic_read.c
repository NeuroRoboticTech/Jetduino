//jetduino Example for using the ultrasonic range finder
#include "jetduino.h"
//gcc jetduino_digital_read.c jetduino.c -Wall
int main(void)
{
	int dval;

	//Exit on failure to start communications with the jetduino
	if(init()==-1)
		exit(1);

	while(1)
	{
		dval=ultrasonicRead(4);
		printf("Range: %d\n", dval);
		//Sleep for 100ms
		jet_sleep(100);
	}
   	return 1;
}
