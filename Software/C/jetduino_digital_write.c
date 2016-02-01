//jetduino Example for using the digital write command
#include "jetduino.h"
//gcc jetduino_digital_write.c jetduino.c -Wall
int main(void)
{
	//Exit on failure to start communications with the jetduino
	if(init()==-1)
		exit(1);

	//Set pin mode to output
	pinMode(4,1);
	while(1)
	{
		digitalWrite(4,1);
		jet_sleep(500);
		digitalWrite(4,0);
		jet_sleep(500);
	}
   	return 1;
}
