//jetduino Example for setting/getting dynamixel servo registers
#include "jetduino.h"
//gcc jetduino_digital_read.c jetduino.c -Wall
int main(void)
{
	int dval;
    int i = 0, servo = 1;
    int pin = ARD_D4;

	//Exit on failure to start communications with the jetduino
	if(openJetduino()==-1)
		exit(1);

    printf ("setting return status level to 1\n");
    dynamixelSetRegister(servo, AX_RETURN_LEVEL, 1, 1);

    int ret_level = dynamixelGetRegister(servo, AX_RETURN_LEVEL, 1);
    printf ("return status level: %d\n", ret_level);
/*
    //first get the angle limits
    int cw_limit_orig = dynamixelGetRegister(servo, AX_CW_ANGLE_LIMIT_L, 2);
    int ccw_limit_orig = dynamixelGetRegister(servo, AX_CCW_ANGLE_LIMIT_L, 2);
    printf ("Before: CW Limit: %d, CCW Limit: %d\n", cw_limit_orig, ccw_limit_orig);

    //now set them to something else
    printf ("Setting cw=130, ccw=180\n");
    dynamixelSetRegister(servo, AX_CW_ANGLE_LIMIT_L, 2, 130);
    dynamixelSetRegister(servo, AX_CCW_ANGLE_LIMIT_L, 2, 800);

    //get the angle limits again to check
    int cw_limit = dynamixelGetRegister(servo, AX_CW_ANGLE_LIMIT_L, 2);
    int ccw_limit = dynamixelGetRegister(servo, AX_CCW_ANGLE_LIMIT_L, 2);
    printf ("After: CW Limit: %d, CCW Limit: %d\n", cw_limit, ccw_limit);

    //now reset them back to the original values
    printf ("Resetting angle limits to original values\n");
    dynamixelSetRegister(servo, AX_CW_ANGLE_LIMIT_L, 2, 0);
    dynamixelSetRegister(servo, AX_CCW_ANGLE_LIMIT_L, 2, 1023);

    //get the angle limits again to check
    cw_limit = dynamixelGetRegister(servo, AX_CW_ANGLE_LIMIT_L, 2);
    ccw_limit = dynamixelGetRegister(servo, AX_CCW_ANGLE_LIMIT_L, 2);
    printf ("Reset: CW Limit: %d, CCW Limit: %d\n", cw_limit, ccw_limit);
*/
	closeJetduino();

   	return 1;
}
