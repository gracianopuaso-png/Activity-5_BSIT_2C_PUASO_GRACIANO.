
# 5.0 Laboratory Activity: Stacks and Queues
# Stacks and Queues: Array vs. Linked List

# -------------------- NODE CLASS --------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# -------------------- ARRAY STACK --------------------

class ArrayStack:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow!")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow!")
        value = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.data[self.top]

    def display(self):
        return self.data[:self.top + 1][::-1]


# -------------------- LINKED LIST STACK --------------------

class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow!")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.top.value

    def display(self):
        result = []
        current = self.top
        while current is not None:
            result.append(current.value)
            current = current.next
        return result


# -------------------- CIRCULAR ARRAY QUEUE --------------------

class ArrayQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow!")
        rear = (self.front + self.size) % len(self.data)
        self.data[rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow!")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.data[self.front]

    def display(self):
        result = []
        for i in range(self.size):
            index = (self.front + i) % len(self.data)
            result.append(self.data[index])
        return result


# -------------------- LINKED LIST QUEUE --------------------

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow!")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.front.value

    def display(self):
        result = []
        current = self.front
        while current is not None:
            result.append(current.value)
            current = current.next
        return result


# -------------------- PARENTHESES CHECKER --------------------

def check_balanced(expression):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for character in expression:
        if character in "([{":
            stack.append(character)
        elif character in ")]}":
            if not stack:
                return False
            if stack.pop() != matching[character]:
                return False

    return len(stack) == 0


# -------------------- PRINT QUEUE SIMULATION --------------------

def print_queue_simulation():
    queue = LinkedQueue()

    print("\n===== PRINT QUEUE SIMULATION =====")
    try:
        number = int(input("How many print jobs? "))
        if number < 0:
            print("Please enter zero or a positive number.")
            return

        for i in range(number):
            print(f"\nJob {i + 1}")
            job_id = input("Enter Job ID: ")
            pages = int(input("Enter number of pages: "))
            if pages < 0:
                print("Page count cannot be negative. Job skipped.")
                continue
            queue.enqueue({"id": job_id, "pages": pages})

        print("\n===== WAITING PRINT JOBS (FIFO) =====")
        for job in queue.display():
            print(f"Job ID: {job['id']} | Pages: {job['pages']}")

        print("\n===== PRINTING JOBS =====")
        order = 1
        while not queue.is_empty():
            job = queue.dequeue()
            print(f"Print Order: {order}")
            print(f"Job ID: {job['id']}")
            print(f"Pages: {job['pages']}")
            print("Status: Printed")
            print("-----------------------")
            order += 1

        print("All print jobs completed!")
    except ValueError:
        print("Invalid input. Please enter a valid number of pages/jobs.")


# -------------------- STACK MENU --------------------

def stack_menu(stack):
    while True:
        print("\n===== STACK OPERATIONS =====")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Is Empty?")
        print("5. Is Full?")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                value = input("Enter value: ")
                stack.push(value)
                print("Successfully pushed:", value)
            elif choice == "2":
                print("Popped:", stack.pop())
            elif choice == "3":
                print("Top element:", stack.peek())
            elif choice == "4":
                print("Is Empty:", stack.is_empty())
            elif choice == "5":
                print("Is Full:", stack.is_full())
            elif choice == "0":
                break
            else:
                print("Invalid choice!")

            print("Stack (top to bottom):", stack.display())
        except (IndexError, OverflowError) as error:
            print("Error:", error)
            print("Stack (top to bottom):", stack.display())


# -------------------- QUEUE MENU --------------------

def queue_menu(queue):
    while True:
        print("\n===== QUEUE OPERATIONS =====")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek Front")
        print("4. Is Empty?")
        print("5. Is Full?")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                value = input("Enter value: ")
                queue.enqueue(value)
                print("Successfully enqueued:", value)
            elif choice == "2":
                print("Dequeued:", queue.dequeue())
            elif choice == "3":
                print("Front element:", queue.peek_front())
            elif choice == "4":
                print("Is Empty:", queue.is_empty())
            elif choice == "5":
                print("Is Full:", queue.is_full())
            elif choice == "0":
                break
            else:
                print("Invalid choice!")

            print("Queue (front to rear):", queue.display())
        except (IndexError, OverflowError) as error:
            print("Error:", error)
            print("Queue (front to rear):", queue.display())


# -------------------- MAIN PROGRAM --------------------

def main():
    while True:
        print("\n================================")
        print("     STACKS AND QUEUES SYSTEM")
        print("================================")
        print("1. Array Stack")
        print("2. Linked List Stack")
        print("3. Circular Array Queue")
        print("4. Linked List Queue")
        print("5. Parentheses Checker")
        print("6. Print Queue Simulation")
        print("0. Exit")

        choice = input("Select implementation: ")

        try:
            if choice == "1":
                capacity = int(input("Enter stack capacity: "))
                stack_menu(ArrayStack(capacity))
            elif choice == "2":
                stack_menu(LinkedStack())
            elif choice == "3":
                capacity = int(input("Enter queue capacity: "))
                queue_menu(ArrayQueue(capacity))
            elif choice == "4":
                queue_menu(LinkedQueue())
            elif choice == "5":
                expression = input("Enter parentheses expression: ")
                if check_balanced(expression):
                    print("Result: Balanced")
                else:
                    print("Result: Not Balanced")
            elif choice == "6":
                print_queue_simulation()
            elif choice == "0":
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as error:
            print("Input error:", error)


# -------------------- RUN PROGRAM --------------------

if __name__ == "__main__":
    main()
