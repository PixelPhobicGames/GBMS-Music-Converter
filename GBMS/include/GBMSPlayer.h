#include <gb/gb.h>
#include <stdint.h>
#include <stdio.h>

static UINT8 MusicCounter1 = 0;
//static UINT8 MusicCounter2 = 0;
//static UINT8 MusicCounter3 = 0;
//static UINT8 MusicCounter4 = 0;

static UINT8 FrameCounter = 0;




// Different Sounds To Use

// Example Usage: PlayMusic(SquareWave, MyMusic , MyMusicSize);

// ONLY SUPPORTS SQUARE AT THE MOMENT 


// Play Music Function

void PlayMusicSquareWave(unsigned char Music[] , UINT8 Reverb , UINT8 Delay , UINT8 Size) {

	if (Music[MusicCounter1] == 0){
		NR52_REG = 0x00;
	}
	else {
		NR52_REG = 0x80;
	}

	NR51_REG = 0x11;
	NR50_REG = 0x77;

	NR10_REG = 0x00;
	NR11_REG = 0x90;
	NR12_REG = Reverb;
	NR13_REG = Music[MusicCounter1];
	NR14_REG = 0x80 + Music[MusicCounter1 + 1];


	if (MusicCounter1 >= Size){
		MusicCounter1 = 0;
	}

    if (FrameCounter != Delay){ // This is All Assuming the Game Runs at 60FPS 
        FrameCounter ++;
    }
    else{
		FrameCounter = 0;
        MusicCounter1 += 2;
    }

    if (MusicCounter1 == 248){ // Cant Go Over the 8Bit Int Limit 
        MusicCounter1 == 0;
    }

	// Use Multiple 8bit MusicCounters to unlimit the Size
}

/*
void PlayMusicTriangleWave(unsigned char Music[] , UINT8 Delay , UINT8 Size) {

	if (Music[MusicCounter1] == 0){
		NR52_REG = 0x00;
	}
	else {
		NR52_REG = 0x80;
	}

	NR51_REG = 0x11;
	NR50_REG = 0x77;

	NR10_REG = 0x00;
	NR11_REG = 0x90;
	NR12_REG = 0xC4;
	NR13_REG = Music[MusicCounter1];
	NR14_REG = 0x80 + Music[MusicCounter1 + 1];


	if (MusicCounter1 >= Size){
		MusicCounter1 = 0;
	}

    if (FrameCounter != Delay){ // This is All Assuming the Game Runs at 60FPS 
        FrameCounter ++;
    }
    else{
		FrameCounter = 0;
        MusicCounter1 += 2;
    }

    if (MusicCounter1 == 248){ // Cant Go Over the 8Bit Int Limit 
        MusicCounter1 == 0;
    }
}


void PlayMusicNoise(unsigned char Music[] , UINT8 Delay , UINT8 Size) {

	if (Music[MusicCounter1] == 0){
		NR52_REG = 0x00;
	}
	else {
		NR52_REG = 0x80;
	}

	NR51_REG = 0x11;
	NR50_REG = 0x77;

	NR10_REG = 0x00;
	NR11_REG = 0x90;
	NR12_REG = 0xC4;
	NR13_REG = Music[MusicCounter1];
	NR14_REG = 0x80 + Music[MusicCounter1 + 1];


	if (MusicCounter1 >= Size){
		MusicCounter1 = 0;
	}

    if (FrameCounter != Delay){ // This is All Assuming the Game Runs at 60FPS 
        FrameCounter ++;
    }
    else{
		FrameCounter = 0;
        MusicCounter1 += 2;
    }

    if (MusicCounter1 == 248){ // Cant Go Over the 8Bit Int Limit 
        MusicCounter1 == 0;
    }
}

*/