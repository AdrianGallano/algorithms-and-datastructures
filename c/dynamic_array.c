#include <stdio.h>

/* ||| DISCONTINUED THIS FOR A WHILE I NEED TO LEARN MEMORY ALLOCATION FIRST ||| */

/*
Implementation for:
access
insert
search
append
delete

Notes:
|| this could be more but i'll only look into the fundamentals
|| and i decided to use only 1 array

||| n = data
*/

int len = 0;
int capacity = 0;
int arr[]={};
int appendData(int n);
int deleteData(int n);
int insertData(int n, int whereTo);
int searchData(int n);

int main(void)
{

  // Appending O(1)
  appendData(5);
  appendData(10);
  appendData(15);
  appendData(20);
  appendData(25);

  // Access O(1)
  printf("\nAccess\n");
  printf("length: %i\n", len);
  printf("capacity: %i\n", capacity);
  printf("arr[0]: %i\n", arr[0] );

  // Searching O(n)
  printf("\nSearch\n");
  searchData(25);

  // printing all data
  printf("\nPrinting All Data\n");
  for (int i = 0; i < len; i++)
  {
    printf("array data %i: %i\n", i, arr[i]);
  }

  return 0;
}

int appendData(int n)
{
  if (len + 1 > capacity)
  {
    if (len == 0)
    {
      capacity = 1;
    }
    else
    {
      capacity *= 2;
    }
    
  }
  arr[len++] = n;
  return 0;
}

int searchData(int n){
  for (int i = 0; i < len; i++)
  {
    if(arr[i] == n){
      printf("array data %i: %i\n", i, arr[i]);
      return i;
    }
  }
  printf("cannot find %i",n);
  return 0;
}

int deleteData(int n)
{

  return 0;
}

int insertData(int n, int whereTo)
{
  // so the first thing is i need to move my array to the left
  // then place my n in whereTo
  // 0 1 3 2 3 4 5 6

  return 0;
}

