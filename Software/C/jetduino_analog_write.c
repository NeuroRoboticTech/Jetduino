//jetduino Example for using the analog write
#include "jetduino.h"
//gcc jetduino_analog_write.c jetduino.c -Wall
int main(void)
{
    int i = 0;
	int j = 0;
	int pin = ARD_D4;

	//Exit on failure to start communications with the jetduino
	if(openJetduino()==-1)
		exit(1);

	for(j=0; j<2000; j++)
	{
		for(i=0;i<255;i++)
		{
			printf("%d\n", i);
			//Write the PWM value
			analogWrite(pin, i);
			//Sleep for 10ms
			jet_sleep(50);
		}
	}

	closeJetduino();

   	return 1;
}
