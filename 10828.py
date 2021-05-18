class stack :
    
    def __init__(self, length=10000):
        self.items = []
        self.top = 0
        self.max = length

    def push(self, x):
        self.top += 1
        self.items.append(x)
        
    def pop(self):
        if self.top == 0 :
            print("-1")
        else :
            self.top -= 1
            self.items.pop()
    
    def size(self):
        print(self.top)

    def empty(self):
        if self.top == 0 : print("1")
        else : print("0")

    def top(self):
        if self.top == 0 : print("-1")
        else :
            result = self.items[self.top-1]
            print(result)


a = stack()
command_num = input()
commands = []

for i in range(int(command_num)):
    commands[i] = input()
    a.commands[i]
