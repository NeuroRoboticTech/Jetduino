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

	for(i=0; i<10; i++)
	{
		printf("Moving to 1023 at 100.\n");
        dynamixelMove(1, 1023, 100);
		//Sleep for 2 s
		jet_sleep(2000);

		printf("Moving to 10 at 1000.\n");
        dynamixelMove(1, 10, 1000);
		//Sleep for 2 s
		jet_sleep(2000);
	}

	closeJetduino();

   	return 1;
}
