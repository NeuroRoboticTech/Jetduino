//jetduino Example for using the digital read command
#include "jetduino.h"
//gcc jetduino_digital_read.c jetduino.c -Wall
int main(void)
{
	int dval;
    int i = 0;
    int buttonPin = JET_PU2;
    int ledPin = ARD_D4;

	//Exit on failure to start communications with the jetduino
	if(openJetduino()==-1)
		exit(1);

	//Set pin mode to input
	pinMode(buttonPin, INPUT_PIN);
	pinMode(ledPin, OUTPUT_PIN);

	for(i=0; i<2000; i++)
	{
	    //Read from the digital input.
		dval=digitalRead(buttonPin);
		printf("Digital read %d\n", dval);

        //Write that value back out to the led.
		digitalWrite(ledPin, dval);

		//Sleep for 50ms
		jet_sleep(50);
	}

	closeJetduino();

   	return 1;
}
