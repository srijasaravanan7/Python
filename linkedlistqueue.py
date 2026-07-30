class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
front=None
rear=None
def enqueue(value):
    global front,rear
    new_node=Node(value)
    new_node.next=None
    if rear is None:
        front=new_node
        rear=new_node
    else:
        rear.next=new_node
        rear=new_node
    print(f"Car '{value}' entered the parking queuee")
def dequeue():
    global front,rear
    if front is None:
        print("Queue is Empty")
        return
    temp=front
    front=front.next
    print(f"Car '{temp.data}' exited the parking queue")
    del temp
    if front is None:
        rear=None
def show():
    if front is None:
        print(f"Queue is Empty")
        return
    temp=front
    print("Cars current in queue:",end=" ")
    while temp.next!=None:
        print(f"{temp.data}--->",end=" ")
        temp=temp.next
    print(f"{temp.data}--->NULL")
def main():
    while True:
        print("\n---Car Parking Queue Menu(Linked List)---")
        print("1.Enqueue(Car Entry)")
        print("2.Dequeue(Car Exit)")
        print("3.Show Queue")
        print("4.Exit")
        choice=int(input("Enter your choice"))
        if choice==1:
            value=input("Enter car number to enqueue")
            enqueue(value)
        elif choice==2:
            dequeue()
        elif choice==3:
            show()
        elif choice==4:
            print("Exiting program")
            break
        else:
            Print("Invalid choice.please try again")
main()

