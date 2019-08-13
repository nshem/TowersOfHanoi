# tower of Hanoi solutions validator

##### Requirements

<u>language</u>: python

<u>input</u>: .txt, first num is of disks



##### It should

- [x] parse .txt to array
- [x] slice the first num to initialize game
- [x] stop when the first illegal move happens
- [x] if all was legal, check if the solution is whole (no more and no less steps then needed)

###### if i'll have time

- [ ] encapsulate functions



##### Entities

game (num of disks, __def win)

rod (rod_id, disks, weight)

~~disk~~ (one prop obj)



##### steps

- [x] create objects, structure. cmd input turn input
- [x] full list (num of disks, moves) input (recursion)
- [x] text file input
- [ ] unit tests



##### tests (manual)

- [x] check user input (max+min rods in moves)
- [x] static move (33/22/11..)
- [x] move to empty spot
- [x] move from empty spot
- [x] not a win if all on the first rod, as well as no moves
- [x] two digits disks number
- [x] empty files
- [x] files with unexpected format





