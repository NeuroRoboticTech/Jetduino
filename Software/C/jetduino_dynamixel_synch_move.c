//jetduino Example for synchronously moving dynamixel servos using the jetduino.
#include "jetduino.h"
//gcc jetduino_digital_read.c jetduino.c -Wall
int main(void)
{
	int dval;
    int i = 0, servo_a = 1, servo_b = 2;
    int pin = ARD_D4;

	//Exit on failure to start communications with the jetduino
	if(openJetduino()==-1)
		exit(1);

    //set the dynamixels so they only returns back data for read commands.
    printf ("setting return status level to 1\n");
    dynamixelSetRegister(servo_a, AX_RETURN_LEVEL, 1, 1);
    dynamixelSetRegister(servo_b, AX_RETURN_LEVEL, 1, 1);

	for(i=0; i<10; i++)
	{

        dynamixelStartSynchMove();
        printf ("Moving 1 to 1023 at 100\n");
        printf ("Moving 2 to 10 at 1000\n");
        dynamixelAddSynchMove(servo_a, 1023, 200);
        dynamixelAddSynchMove(servo_b, 10, 1000);
        dynamixelExecuteSynchMove();
        jet_sleep(4000);

        dynamixelStartSynchMove();
        printf ("Moving 1 to 10 at 100\n");
        printf ("Moving 2 to 1023 at 1000\n");
        dynamixelAddSynchMove(servo_a, 10, 1000);
        dynamixelAddSynchMove(servo_b, 1023, 200);
        dynamixelExecuteSynchMove();
        jet_sleep(4000);
	}

	closeJetduino();

   	return 1;
}
