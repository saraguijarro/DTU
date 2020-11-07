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

int x = 0;
int y = 0;

void
kprints(const char* string)
{
  while (*string != 0)
  {
    if (*string == '\n')
    {
      x = 0;
      y++;
    }
    else
    {
      screen_pointer->positions[y][x].character = *string;
      screen_pointer->positions[y][x].attribute = 0xF0;
      x++;
    }
    string++;
  }
}

void
kprinthex(const register uint32_t value)
{
  uint32_t n = value;
  char hex[100];
  int i = 0;

  while(n != 0)
  {
    int remainder = n%16;
    if (remainder < 10)
    {
      hex[i] = (char) remainder + 48;
    }
    else
    {
      hex[i] = (char) remainder + 55;
    }
    i++;
    n = n/16;
  }

  hex[i] = '\n';
  kprints(&hex[0]);
}
