
/**************************************************

file: demo_rx.c
purpose: simple demo that receives characters from
the serial port and print them on the screen,
exit the program by pressing Ctrl-C

compile with the command: gcc demo_rx.c rs232.c -Wall -Wextra -o2 -o test_rx

**************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

#include "rs232.h"

int main()
{
  int n,
      cport_nr=17,        /* /dev/ttyS0 (COM1 on windows) */
      bdrate=9600;       /* 9600 baud */

  uint8_t *buf;
  buf=malloc(8192);

  char mode[]={'8','N','1',0};


  if(RS232_OpenComport(cport_nr, bdrate, mode))
  {
    printf("Can not open comport\n");

    return(0);
  }
int c=0;
int k =0;
  while(1)
  {
    n = RS232_PollComport(cport_nr, buf, 8191);

    if(n > 0)
    {
      buf[n] = 0;   /* always put a "null" at the end of a string! */

//      for(r=0; r < n; r++)
//     {
//        if(buf[r] < 32)  /* replace unreadable control-codes by dots */
//        {
//          buf[r] = '.';
//        }
//      }
	//printf("\nreceived %i bytes: 0x",n);
	//printf("\n");
	while (k < n){
      		printf("%x ", buf[k]);
	k++;
	}
	printf("\n");
	k = 0;
	c++;
	if (c==2)
		break;
    }

#ifdef _WIN32
    Sleep(1000);
#else
    usleep(100000);  /* sleep for 1000 milliSeconds */
#endif
  }

  free (buf);
  buf = NULL;
  return(0);
}

