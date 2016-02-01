//Jetduino Example for using the analog read
#include "jetduino.h"

int main(void)
{
	int adata;

	//Exit on failure to start communications with the Jetduino
	if(init()==-1)
		exit(1);

	while(1)
	{
        adata=analogRead(0);
        printf("analog read %d\n",adata);
        if(adata==-1)
            printf("IO Error");
        usleep(10000);
	}
   	return 1;
}
