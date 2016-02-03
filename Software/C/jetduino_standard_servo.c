//Jetduino Example for controlling and reading from a standard servo
#include "jetduino.h"

#define SERVO_PIN 4

int main(void)
{
	int adata;

	//Exit on failure to start communications with the Jetduino
	if(init()==-1)
		exit(1);

    printf("Attaching to servo\n");
    servoAttach(SERVO_PIN);
    usleep(100000);

    printf("Moving servo to angle 0.\n");
    servoWrite(SERVO_PIN, 0);
    usleep(100000);

    printf("Reading servo angle.\n");
    int cur_angle = servoRead(SERVO_PIN);
    printf("Angle: %d\n", cur_angle);
    usleep(1000000);

    printf("Moving servo to angle 180.\n");
    servoWrite(SERVO_PIN, 180);
    usleep(100000);

    printf("Reading servo angle.\n");
    cur_angle = servoRead(SERVO_PIN);
    printf("Angle: %d\n", cur_angle);
    usleep(1000000);

    int num=0, angle=0;
    for(num=0; num<5; num++)
	{
        printf("Moving servo cycle %d\n", num);

        for(angle=0; angle<180; angle++)
        {
            servoWrite(SERVO_PIN, angle);
            usleep(10000);
        }

        usleep(1000000);
	}

    printf("Detaching from servo\n");
    servoDetach(SERVO_PIN);

   	return 1;
}
