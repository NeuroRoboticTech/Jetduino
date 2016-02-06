//jetduino Example for using the ultrasonic range finder
#include "jetduino.h"
//gcc jetduino_digital_read.c jetduino.c -Wall
int main(void)
{
	int dval;
    int i = 0;
    int pin = ARD_D4;

	//Exit on failure to start communications with the jetduino
	if(openJetduino()==-1)
		exit(1);

	for(i=0; i<2000; i++)
	{
		dval=ultrasonicRead(pin);
		printf("Range: %d\n", dval);
		//Sleep for 100ms
		jet_sleep(100);
	}

	closeJetduino();

   	return 1;
}
