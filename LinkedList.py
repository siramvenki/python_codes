# A simple Python program to introduce a linked list 

# Node class 
class Node: 

	# Function to initialise the node object 
	def __init__(self, data): 
		self.data = data # Assign data 
		self.next = None # Initialize next as null 


# Linked List class contains a Node object 
class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None

	def push(self,data):
		new_node=Node(data);
		if self.head is None:
			self.head=new_node
			return
		new_node.next=self.head
		self.head=new_node

	def insert(self,position,data):
		new_node=Node(data)
		len=0
		last=self.head
		while (last.next):
			len=len+1
			last=last.next
		size=len
		# print("size of linked list ",size)
		if size<position:
			print("ENTER CORRECT position")
			return
		i=0
		prevnode=self.head
		while i<position:
			prevnode=prevnode.next
			i=i+1
		temp=prevnode.next
		prevnode.next=new_node
		new_node.next=temp



	def append(self,data):
		new_node=Node(data);

		if self.head is None:
			self.head=new_node
			return
		last = self.head 
		while (last.next): 
			last = last.next
		last.next=new_node

	def delBeg(self):
		temp=self.head
		self.head=temp.next
		llist=temp.next

		temp=None
		return llist
	def print(self):
		temp=self.head
		while temp:
			print(temp.data)
			temp=temp.next

	def deleteAt(self,position):
		i=1
		ll=self.head
		while(ll.next is not None and i<position):
			# print(i)
			prevnode=ll
			ll=ll.next
			i=i+1
		prevnode.next=ll.next
		ll=None

	def deleteTail(self):
		ll=self.head
		while(ll.next.next is not None):
			ll=ll.next
		ll.next=None
			
if __name__=='__main__': 

	llist = LinkedList() 

	llist.head = Node(1) 
	second = Node(2) 
	third = Node(3) 


	llist.head.next = second;
	second.next = third; 
	llist.append(20)
	llist.push(200)
	llist.insert(2,999)
	llist.print()

	print('*******************************')
	# llist.delBeg()
	# llist.deleteAt(3)
	llist.deleteTail()
	# print(llist.head.data)
	llist.print()