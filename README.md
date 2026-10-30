Stacks and Queues

Name: Puaso Graciano A.
Course, Year, and Section: BSIT - 2C

About

This project demonstrates stacks and queues in Python using arrays/lists and linked nodes. It also includes a balanced-parentheses checker and a simple print-queue simulation.

Files

array_stack.py — stack with a fixed capacitylinked_stack.py — stack implemented with linked nodesarray_queue.py — circular queue with a fixed capacitylinked_queue.py — queue implemented with linked nodesbalanced_parentheses.py — checks matching parentheses, brackets, and bracesprint_queue.py — simulates documents waiting to printmain.py — menu for testing the four data structuresanalysis.md — answers to analysis questionssample_runs.md — example program outputs

Requirements

Python 3No extra packages are required.

Run the programs

Open a terminal in this folder and run:

python main.py

To run the parentheses checker:

python balanced_parentheses.py

To run the print queue:

python print_queue.py

Things to test

Push more than three items into the array stack to see overflow.Pop from an empty stack to see underflow.Enqueue more than three items into the circular queue to see overflow.Dequeue from an empty queue to see underflow.Enqueue A, B, and C; dequeue A and B; then enqueue D and E in a queue with sufficient capacity. The remaining order should follow FIFO.Try {[()]} and ({[}) in the parentheses checker.Add several print jobs and check that the first job added prints first.
