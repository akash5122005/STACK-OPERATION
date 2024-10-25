class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        newnode=node(data)

        if self.head is None:
            self.head = newnode
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=newnode

    def to_string(self):
        current=self.head
        re=[]
        while current:
            re.append(current.data)
            current=current.next
        return "".join(re)
class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items) == 0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.items[-1]

    def pre(self,op):
        if op in ("+","-"):
            return 1 
        elif op in ("*","/"):
            return 2
        elif op in ("^"):
            return 3
        return 0                       

def infix_to_postfix(exp):

        stack = Stack()
        postfix=LinkedList()

        for char in exp:
            if char.isalnum():
                postfix.append(char)
            elif char in("+","-","*","/","^"):
                while(not stack.is_empty() and stack.pre(stack.peek()) >= stack.pre(char)):
                    postfix.append(stack.pop())
                stack.push(char)
            elif char =="(":
                stack.push(char)
            elif char==")":
                while(not stack.is_empty() and stack.peek() !="("):
                    postfix.append(stack.pop())
                stack.pop()

        while not stack.is_empty():
            postfix.append(stack.pop())

        return postfix.to_string()

def main():
    print(infix_to_postfix(input()))

main()    
