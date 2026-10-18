stack = []
MAX = 5

def push():
    if len(stack) == MAX:
        print("Stack Overflow")
    else:
        value = int(input("Enter value: "))
        stack.append(value)
        print(value, "pushed into stack")

def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print(stack.pop(), "popped from stack")

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:", stack[::-1])

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        push()
    elif choice == "2":
        pop()
    elif choice == "3":
        display()
    elif choice == "4":
        print("Program ended")
        break
    else:
        print("Invalid choice")