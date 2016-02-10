//jetduino Example for moving dynamixel servos using the jetduino.
#include "jetduino.h"
//gcc jetduino_digital_read.c jetduino.c -Wall
int main(void)
{
	int dval;
    int i = 0, num = 0, pos = 0, servo = 1;
    int pin = ARD_D4;

	//Exit on failure to start communications with the jetduino
	if(openJetduino()==-1)
		exit(1);

    //set the dynamixel so it only returns back data for read commands.
    printf ("setting return status level to 1\n");
    dynamixelSetRegister(servo, AX_RETURN_LEVEL, 1, 1);

    printf ("Move to 0 at fastest speed\n");
    dynamixelMove(servo, 0, 0);
    jet_sleep(1000);

    printf ("Move to 1023 slowly\n");
    dynamixelMove(servo, 1023, 200);
    jet_sleep(500);

    printf ("stop the servo at its current position.\n");
    dynamixelStop(servo);
    jet_sleep(1000);

	for(i=0; i<10; i++)
	{
		printf("Moving to 1023 at 100.\n");
        dynamixelMove(servo, 1023, 100);

        for(num=0; num<20; num++)
        {
            jet_sleep(100);
            pos = dynamixelGetRegister(servo, AX_PRESENT_POSITION_L, 2);
            printf ("Pos: %d\n", pos);
        }

		printf("Moving to 10 at 1000.\n");
        dynamixelMove(servo, 10, 1000);

        for(num=0; num<20; num++)
        {
            jet_sleep(100);
            pos = dynamixelGetRegister(servo, AX_PRESENT_POSITION_L, 2);
            printf ("Pos: %d\n", pos);
        }
	}

	closeJetduino();

   	return 1;
}
