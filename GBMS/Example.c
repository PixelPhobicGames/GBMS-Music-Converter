#include "include/GBMSPlayer.h"

#include <stdbool.h>

unsigned char Music[] = {1627 , 6 ,0 , 0,1602 , 6 ,0 , 0,1627 , 6 ,0 , 0,1627 , 6 ,0 , 0,0 , 0,0 , 0,1673 , 6 ,0 , 0,0 , 0,1602 , 6 ,0 , 0,1627 , 6 ,0 , 0,1602 , 6 ,0 , 0,1627 , 6 ,0 , 0,1627 , 6 ,0 , 0,0 , 0,1602 , 6 ,0 , 0,1602 , 6 ,0 , 0,1627 , 6 ,0 , 0,1602 , 6 ,0 , 0,1627 , 6 ,0 , 0,1627 , 6 ,0 , 0,0 , 0,1673 , 6 ,0 , 0,1602 , 6 ,0 , 0,1627 , 6 ,0 , 0,1673 , 6 ,0 , 0,1767 , 6 ,0 , 0,1750 , 6 ,0 , 0,0 , 0,1673 , 6 ,0 };

#define MusicLength 104

void main(){
	while (true){
		PlayMusicSquareWave(Music , 0xF3 , 10 , MusicLength);
		wait_vbl_done();
	}
}