//jetduino Example for using the analog write
#include "jetduino.h"
//gcc jetduino_analog_write.c jetduino.c -Wall
int main(void)
{
	int i;

	//Exit on failure to start communications with the jetduino
	if(init()==-1)
		exit(1);

	while(1)
	{
		for(i=0;i<255;i++)
		{
			printf("%d\n", i);
			//Write the PWM value
			analogWrite(4,i);
			//Sleep for 10ms
			jet_sleep(50);
		}
	}
   	return 1;
}
