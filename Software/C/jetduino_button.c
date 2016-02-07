//jetduino Example for using the digital read and write commands
#include "jetduino.h"
//gcc jetduino_digital_write.c jetduino.c -Wall
int main(void)
{
    int i = 0;
    int button = ARD_D4;
    int led = ARD_D6;

	//Exit on failure to start communications with the jetduino
	if(openJetduino()==-1)
		exit(1);

	//Set pin modes
	pinMode(button, INPUT_PIN);
	pinMode(led, OUTPUT_PIN);
	for(i=0; i<2000; i++)
	{
		printf("i: %d\n", i+1);
        int val = digitalRead(button);
		printf("LED: %d\n", val);
		digitalWrite(led, val);
		jet_sleep(100);
		printf("\n");
	}

	closeJetduino();

   	return 1;
}
