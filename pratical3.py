class node:
    def __init__(self, patient_id, name, priority):
        self.id = patient_id
        self.data = name
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    # Add Patient
    def enqueue(self, new_node):

        if self.front == None:
            self.front = new_node
            return

        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return

        else:
            temp = self.front

            while temp.next and temp.next.priority <= new_node.priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

        print("Patient added successfully!")


    # Display Next Patient
    def display_next(self):

        if self.front == None:
            print("Queue is empty")

        else:
            print("\nNext Patient to be Treated:")
            print("Patient ID:", self.front.id)
            print("Patient Name:", self.front.data)
            print("Priority:", self.front.priority)


    # Remove Treated Patient
    def dequeue(self):

        if self.front:
            temp = self.front

            print("Patient treated:", temp.data)

            self.front = self.front.next

        else:
            print("Queue is empty")


    # Display All Patients
    def display(self):

        if self.front == None:
            print("Queue is empty")

        else:
            temp = self.front

            print("\nWaiting Patients:")
            print("ID\tName\tPriority")

            while temp:
                print(temp.id, "\t", temp.data, "\t", temp.priority)
                temp = temp.next


# Create Priority Queue
pq = PriorityQueue()

while True:

    print("\n===== HOSPITAL EMERGENCY MANAGEMENT =====")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Treated Patient")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        patient_id = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if priority >= 1 and priority <= 3:
            pq.enqueue(node(patient_id, name, priority))
        else:
            print("Invalid Priority!")

    elif choice == 2:
        pq.display_next()

    elif choice == 3:
        pq.dequeue()

    elif choice == 4:
        pq.display()

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
