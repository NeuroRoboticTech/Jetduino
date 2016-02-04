//Jetduino Example for using the Grove temperature sensor
#include "jetduino.h"

int main(void)
{
	float temp;

	//Exit on failure to start communications with the Jetduino
	if(init()==-1)
		exit(1);

	while(1)
	{
        temp=temperatureRead(0, 2);
        printf("Temperature: %f\n",temp);
        if(temp==-1)
            printf("IO Error");
        usleep(100000);
	}
   	return 1;
}
