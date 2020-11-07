/* Copyright (c) 1997-2017, FenixOS Developers
   All Rights Reserved.

   This file is subject to the terms and conditions defined in
   file 'LICENSE', which is part of this source code package.
 */

/*! \file video.c This file holds implementations of functions
  presenting output to the VGA screen. */
#include <stdint.h>

/*! Max number of columns in the VGA buffer. */
#define MAX_COLS                (80)
/*! Max number of columns in the VGA buffer. */
#define MAX_ROWS                (25)

struct screen_position
{
 unsigned char character; /*!< The character part of the byte tuple used for
                               each screen position. */
 unsigned char attribute; /*!< The character part of the byte tuple used for
                               each screen position. */
};
/*!< Defines a VGA text mode screen position. */

struct screen
{
 struct screen_position positions[MAX_ROWS][MAX_COLS];
 /*!< The VGA screen. It is organized as a two dimensional array. */
};
/*!< Defines a VGA text mode screen. */

/*! points to the VGA screen. */
static struct screen* const
screen_pointer = (struct screen*) 0xB8000;

int x = 0; //Initialize the x-cooridnate to zero
int y = 0; //Initialize the y-cooridnate to zero

void
kprints(const char* string)
{
  while (*string != 0) //Verifies the whole string is read
  {
    if (*string == '\n')
    {
      x = 0; //New line starts always furthest left side of screen
      y++; //Jump line so move down the y-axis
    }
    else
    {
      screen_pointer->positions[y][x].character = *string; //Pointer to "character" which correpsonds to the ASCII code byte of the character studied found with the pointer string
      screen_pointer->positions[y][x].attribute = 0xF0; //Pointer to "attribute" which corresponds to the colour of the text printed (in this case 0xF0)
      x++; //Print string so move down the x-axis
    }
    string++; //Pointer string moves to the next position
  }
}

void
kprinthex(const register uint32_t value)
{
  int n = value;
  int count = 0;
  while(n != 0)
  {
    n = n/10; //Computation to determine the number of digits the "value" has
    count++; //The int "count" is used to set the length of the hexadecimal number
   }

  uint32_t val = value;
  char hex[count]; //Char array "hex" used to store the hexadecimal number
  int i = 0;
  
  //Determine the  hexadecimal value using the following calculations
  while(val != 0)
  {
    int remainder = val%16;
    if (remainder < 10)
    {
      hex[i] = (char) (remainder + 48);
    }
    else
    {
      hex[i] = (char) (remainder + 55);
    }
    i++;
    val = val/16;
  }

  hex[i] = '\n'; //Jumps line after printing the hexadecimal
  kprints(&hex[0]); //Prints the hexadecimal
}

