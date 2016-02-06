//Jetduino Example for using the analog read
#include "jetduino.h"

int main(void)
{
	int adata;
    int i = 0;
    int pin = ARD_A0;

	//Exit on failure to start communications with the Jetduino
	if(openJetduino()==-1)
		exit(1);

	for(i=0; i<2000; i++)
	{
        adata=analogRead(ARD_A0);
        printf("analog read %d\n",adata);
        if(adata==-1)
            printf("IO Error");
        usleep(10000);
	}

	closeJetduino();

   	return 1;
}
