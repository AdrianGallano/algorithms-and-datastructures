#include <stdio.h>

int main(){
  int static_array_size = 5;
  int static_array[static_array_size];

  // Access O(1)
  static_array[0] = 1;
  static_array[1] = 2;
  static_array[2] = 3;
  static_array[3] = 4;
  static_array[4] = 5;

  // Search O(n)
  int find = 5;
  for(int i = 0; i < static_array_size; i++){
    if(static_array[i] == find){
      return static_array[find] + " Found in " + i;
    }
  }

  // Deletion N/A as you do it via access 
  static_array[1] = NULL;
  // you also cannot modify the size of the array only the allocation 
  
  // Append N/A you cannot change the size of the array
  return 0;
}