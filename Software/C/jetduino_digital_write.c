//jetduino Example for using the digital write command
#include "jetduino.h"
//gcc jetduino_digital_write.c jetduino.c -Wall
int main(void)
{
    int i = 0;
    //int pin = ARD_D4;
    int pin = JET_PU1;

	//Exit on failure to start communications with the jetduino
	if(openJetduino()==-1)
		exit(1);

	//Set pin mode to output
	pinMode(pin, OUTPUT_PIN);
	for(i=0; i<20; i++)
	{
		printf("i: %d\n", i+1);
		printf("LED on\n");
		digitalWrite(pin, HIGH);
		jet_sleep(500);
		printf("LED off\n");
		digitalWrite(pin, LOW);
		jet_sleep(500);
		printf("\n");
	}

	closeJetduino();

   	return 1;
}
