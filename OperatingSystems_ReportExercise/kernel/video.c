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

void
kprints(const char* string)
{
  int Ax, Ay = 0;
  while (*string)
  {
    uint16_t *ptr; //short
    uint8_t s; //char
    *string = &s;
    if (string == '/n')
    {
      Ax = 0;
      Ay++;
    }
    else if (string >= ' ')
    {
      ptr = screen_pointer + (Ay * MAX_COLS + Ax);
      *ptr = (0xF0 << 8) | string;
      //0xF0 = 11110000 in binary, shifts so that pointer *ptr = 0
      Ax++;
    }
    string++;
  }
  return NULL;
}
    
}

void
kprinthex(const register uint32_t value)
{
 kprint(char toHex(value));
}

toHex(uint32_t n)
{
  char hex[100]; //char array storing the hexadecimal number
  
  int i = 0;
  while (n != 0)
  {
    int remainder = 0;
    remainder = n%16;
    if (remainder < 10)
    {
      hex[i] = (char) (remainder+48);
      i++;
    }
    else
    {
      hex[i] = (char) (remainder+55);
      i++;
    }
    n = n/16;
  }
  
  for (int j = i-1; j >= 0; j--)
  {
    return hex[j]; //hexadecimal number array in reverse order
  }
}
