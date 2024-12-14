# Buddy-System-Memory-Allocator

This repository contains a Python implementation of the Buddy System, a dynamic memory allocation technique used to efficiently manage memory blocks.  

## Overview  

The Buddy System minimizes fragmentation by splitting and merging memory blocks into sizes that are powers of 2.
This project is a simulation of the Buddy Memory Allocation System, a dynamic memory management technique widely used in operating systems. The program demonstrates the allocation and deallocation of memory using a binary tree structure to minimize fragmentation and ensure efficient utilization of memory blocks.


### Features  
- **Dynamic Allocation:** Handles memory requests of varying sizes.  
- **Tree-Based Visualization:** View the memory map with detailed node information (allocated, divided, or free).  
- **Efficient Deallocation:** Reclaim and merge memory blocks when no longer needed.  
- **Simple CLI Interface:** User-friendly console-based interface for interaction.  

### Usage
#### Menu Options:
##### 1. Allocate Process into Memory:

- Specify the size of the memory request.
- The system attempts to allocate memory based on availability and the buddy system rules.

##### 2. Remove Process from Memory:

- Specify the size of the process to deallocate.
- The system reclaims memory and merges adjacent blocks when possible.

##### 3. Tree Structure of Memory Allocation Map:

- View the current memory allocation as a tree, showing the state of each block.

##### 4. Exit:

- Close the application. 

---

## Getting Started  

### Prerequisites  
- Python 3.7 or higher installed on your system.  

### Installation  
1. Clone this repository:  
   
    git clone https://github.com/Thafani24/Buddy-System-Memory-Allocator.git

2. Navigate to the project directory:

    cd Buddy-System-Memory-Allocator

3. Run the script:
    python buddy_system.py

> **Follow the on-screen output to observe memory allocation and deallocation.**

#### Author
- Developed as part of a university project to explore dynamic memory allocation techniques. Contributions and feedback are welcome!


