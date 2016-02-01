//jetduino Example for using the digital read command
#include "jetduino.h"
//gcc jetduino_digital_read.c jetduino.c -Wall
int main(void)
{
	int dval;

	//Exit on failure to start communications with the jetduino
	if(init()==-1)
		exit(1);

	//Set pin mode to input
	pinMode(4,0);
	while(1)
	{
		dval=digitalRead(4);
		printf("Digital read %d\n", dval);
		//Sleep for 50ms
		jet_sleep(50);
	}
   	return 1;
}
