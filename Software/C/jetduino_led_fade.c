//jetduino Example for using the analog write
#include "jetduino.h"
//gcc jetduino_analog_write.c jetduino.c -Wall
int main(void)
{
    int i = 0;
    int j = 0;
    int pot = ARD_A0;
    int led = ARD_D4;
    int oldVal = -1;
    int val = 0;
    int newVal = 0;

    //Exit on failure to start communications with the jetduino
    if(openJetduino()==-1)
        exit(1);

    pinMode(pot, INPUT_PIN);
    pinMode(led, OUTPUT_PIN);
    
    for(j=0; j<2000; j++)
    {
        // Read in the value from the pot.
        val = analogRead(pot);
        
        // Convert to 8-bit
        newVal = mapValue(val, 0, 1023, 0, 255);

        // Give PWM output to LED if value changed.
        if(newVal != oldVal) 
        {
            analogWrite(led,newVal);
            oldVal = newVal;
            printf("LED: %d\n", i);
        }
        
        jet_sleep(250);
    }

    closeJetduino();

    return 1;
}
