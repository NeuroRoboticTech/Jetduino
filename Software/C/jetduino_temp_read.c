//Jetduino Example for using the Grove temperature sensor
#include "jetduino.h"

#define TEMP_VERSION 2

int main(void)
{
	float temp;
    int i = 0;
    int pin = ARD_A0;

	//Exit on failure to start communications with the Jetduino
	if(openJetduino()==-1)
		exit(1);

	for(i=0; i<2000; i++)
	{
        temp=temperatureRead(pin, TEMP_VERSION);
        printf("Temperature: %f\n",temp);
        if(temp==-1)
            printf("IO Error");
        usleep(100000);
	}

	closeJetduino();

   	return 1;
}
