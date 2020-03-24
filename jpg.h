/********************************************************

jpg file

Author: Muhammed El-Yamani
muhammedelyamani92@gmail.com
March 2020


********************************************************/
#pragma once

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// data type of files
typedef uint8_t BYTE;

// locations of files
char *path_card;
char path_image[100];
char *dir_image = "images/";

// files pointers
FILE *card;
FILE *image;

// variable to check end file
int n_bytes;
// counter for images
int count = 0;

// buffer for read and write 512 bytes from files
BYTE block[512];
// first 4 bytes as header of each 512 block for comparing
//with signature of jpg
BYTE b1, b2, b3, b4;
