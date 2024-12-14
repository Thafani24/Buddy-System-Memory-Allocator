# Initialize a binary tree structure for memory allocation
tree = [0] * 2050

def power(x, y):
    """Calculates x raised to the power y."""
    return x ** y

def segment_alloc(total, req):
    """
    Allocates memory for a process using the buddy system.
    
    Args:
        total: The total size of memory available.
        req: The size of the process to be allocated.
    """
    size = total
    flevel = 0  # Represents the current level in the tree

    # Check if the requested memory exceeds total memory
    if req > size:
        print("\nSystem does not have enough memory!\n")
        return

    # Find the smallest block that can accommodate the requested memory
    while True:
        if req <= size and req > size // 2:
            break
        else:
            size //= 2  # Halve the block size
            flevel += 1  # Move to the next level

    # Find a free node at the determined level to allocate the memory
    for i in range(power(2, flevel) - 1, power(2, flevel + 1) - 1):
        if tree[i] == 0 and can_place(i):
            tree[i] = req  # Allocate memory
            make_divided(i)  # Mark parent nodes as divided
            print("\nSuccessful allocation!\n")
            return

    print("\nDoes not have enough memory!\n")

def can_place(node):
    """
    Checks if the memory node can be allocated.
    
    Args:
        node: The index of the node to check.
    
    Returns:
        True if the node can be allocated, False otherwise.
    """
    while node != 0:  # Traverse up the tree to check parent nodes
        node = (node - 1) // 2 if node % 2 == 0 else node // 2
        if tree[node] > 1:  # If any parent is already allocated, return False
            return False
    return True

def make_divided(node):
    """
    Marks the memory node and its parents as divided.
    
    Args:
        node: The index of the node to mark.
    """
    while node != 0:  # Traverse up the tree to mark parent nodes
        node = (node - 1) // 2 if node % 2 == 0 else node // 2
        tree[node] = 1  # Mark node as divided

def make_free(req):
    """
    Deallocates memory for a process.
    
    Args:
        req: The size of the process to be removed.
    """
    node = 0  # Start at the root node

    # Find the node containing the requested memory size
    while True:
        if tree[node] == req:
            break
        node += 1

    tree[node] = 0  # Free the memory at the node

    # Traverse up the tree and merge free sibling nodes
    while node != 0:
        sibling = (node - 1) if node % 2 == 0 else (node + 1)
        parent = (node - 1) // 2 if node % 2 == 0 else node // 2

        if tree[node] == 0 and tree[sibling] == 0:  # If both siblings are free
            tree[parent] = 0  # Free the parent node
            node = parent
        else:
            break

def printing(total, node):
    """
    Prints the memory allocation map as a tree structure.
    
    Args:
        total: The total size of memory.
        node: The current node being printed.
    """
    if node >= len(tree):  # Stop if node index exceeds tree size
        return

    if node == 0 or tree[(node - 1) // 2] == 1:  # Check if node should be printed
        tab = 0  # Indentation level
        llimit, ulimit = 0, 0  # Level limits

        # Determine the level of the current node
        while True:
            if llimit <= node <= ulimit:
                break
            tab += 1
            llimit, ulimit = ulimit + 1, 2 * ulimit + 2

        print(" " * tab, end="")
        print(f"{total // power(2, tab)}", end="")  # Print block size

        if tree[node] > 1:
            print(f" --> Allocates {tree[node]} ")  # Process allocated
        elif tree[node] == 1:
            print(" --> Divided")  # Block is divided
        else:
            print(" --> Free")  # Block is free

        # Recursively print left and right children
        printing(total, 2 * node + 1)
        printing(total, 2 * node + 2)

def main():
    """
    Main function to handle user interaction with the buddy system.
    """
    print("\nBuddy System Requirements:\n")
    totsize = int(input("Enter total size of memory: "))

    while True:
        # Display menu options
        print("\n1. Allocate process into memory")
        print("2. Remove process from memory")
        print("3. Tree structure for memory allocation map")
        print("4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:  # Allocate memory
            print("\nMemory Allocation:\n")
            req = int(input("Enter size of process: "))
            segment_alloc(totsize, req)

        elif choice == 2:  # Deallocate memory
            print("\nMemory Deallocation:\n")
            req = int(input("Enter size of process to be removed: "))
            make_free(req)

        elif choice == 3:  # Print memory allocation map
            print("\nMemory Allocation Map:\n")
            printing(totsize, 0)

        elif choice == 4:  # Exit program
            break

        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
