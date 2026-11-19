class Node:
    def __init__(self,pid,name,priority):
        self.pid=pid
        self.name=priority
        self.next=None
class priorityque:
    def __init__(self):
        self.front=None

    #adding a patient(enque)
    def enqueue(self,new_node):
        if self.front==None:
            self.front=new_node
            return
        if self.front.priority>new_node.priority:
            new_node.next=self.front
            self.front=new_node
            return
        temp = self.front
        while temp.next and temp.next.priority<=new_node.priority:
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        print("Patient added successfully")

        #Next patient
        def display_next(self):
            if self.front==None:
                print("queue is empty")
            else:
                print("Next patient")
                print("Patient ID:",self.front.pid)
                print("patient Name:",self.front.name)
                print("Priority:",self.front.priority)

        #remove patient
        def dequeue(self):
            if self.front:
                temp=self.front
                print("Patient Treated:")
                print("ID:",temp.pid)
                print("name:",temp.name)
                self.front=self.front.next
            else:
                print("queue is empty")

        #display
        def display_all(self):
            temp = self.front
            if temp == None:
                print("No waiting patient")
                return
            print("patients in priority order:")
            while temp:
                print("ID:",temp.pid
                ,"name:",temp.name,"Priority:",temp.priority)
                temp=temp.next

pq = priorityque()
while True:
    print("Hospital Management")
    print("1.Add Patient")
    print("2.Display next patient")
    print("3.remove patient")
    print("4.Display all patients")
    print("5.Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        pid=int(input("Enter patient ID:"))
        name=int(input("Enter patirnt Name:"))
        pr=int(input("Enter the Priority(1-Critical,2-Serious,3-Normal):"))
        if pr>=1 and pr<=3:
            pq.enqueue(Node(pid,name,pr))
        else:
            print("Invalid Priority")
    elif ch==2:
        pq.display_next()
    elif ch==3:
        pq.dequeue()
    elif ch==4:
        pq.display_all()
    elif ch==5:
        print("Thank you!")
        break
    else:
        print("Invalid choice")


