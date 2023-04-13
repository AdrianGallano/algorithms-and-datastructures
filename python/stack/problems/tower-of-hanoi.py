"""
  haven't figured this one out yet
  maybe after recursion
  game rules: 
  - bigger plates cannot be on top of smaller plates
  - bigger plates cannot be on top if smaller plates exist at its bottom
  - smallest plate must be at the very top
  - three sticks would be use
  - the tower must be move at the 3rd tower in order to complete the game
"""


def computerTotalLoop(n):
  return 2 ** n - 1

if __name__ == "__main__":
    num_of_plates = 4
    total = computerTotalLoop(num_of_plates)
    first_tower = [i for i in reversed(range(3, num_of_plates + 3))]
    second_tower = []
    third_tower = []

    for i in range(total):
      pass