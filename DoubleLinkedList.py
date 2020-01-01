class Node():
	"""docstring for Node"""
	def __init__(self,data):
		self.data=data
		self.prev=None
		self.next=None
class DoubleLinkedlist():
	"""docstring for DoubleLinkedlist"""
	def __init__(self):
		self.head= None

	def insertAtBeg(self,data):
		new_node=Node(data)
		new_node.next=self.head
		if self.head is not None:
			self.head.prev=new_node
		self.head=new_node

	def insertAtEnd(self,data):
		new_node=Node(data)
		node=self.head
		while(node.next is not None): 
			last = node 
			node = node.next
		node.next=new_node
		new_node.prev=node
		new_node.next=None

	def insertAt(self,position,data):
		i=0
		new_node=Node(data)
		node=self.head
		while(i<position):
			print('******',i)
			node=node.next
			i=i+1
		temp=node.next
		temp.prev=node
		node.next=new_node
		new_node.prev=node
		new_node.next=temp
		temp.prev=new_node

	def deleteAt():
		pass
	def deleteTail(self):
		node=self.head
		while(node.next is not None): 
			# print(" % d" %(node.data), )
			last = node 
			node = node.next
			# print(node.data)
		temp=node.prev
		temp.next=None
		
	def delBeg(self):
		temp=self.head
		self.head=temp.next
		temp=None
		
	def print(self, node): 

		print("\nTraversal in forward direction")
		while(node is not None): 
			print(" % d" %(node.data), )
			last = node 
			node = node.next
if __name__ == '__main__':
	
	llist = DoubleLinkedlist() 
	llist.insertAtBeg(100)

	llist.insertAtBeg(90)
	llist.insertAtBeg(80)
	llist.insertAtBeg(60)
	llist.insertAtBeg(50)
	llist.insertAtBeg(40)
	llist.print(llist.head)
	print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
	# llist.insertAtEnd(999)
	llist.insertAt(2,70)
	llist.delBeg()
	llist.deleteTail()
	# llist.insert(2,999)
	llist.print(llist.head)

	print('*******************************')
	# llist.delBeg()
	# llist.deleteAt(3)
	# llist.deleteTail()
	# print(llist.head.data)
	# llist.print()
		
		