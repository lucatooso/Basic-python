class stack:
    def __init__(self):
        self.stack =[]
        self.maxsize =5
    def isEmpty(self):
        return self.stack == []
    def push(self,data):
        if self.size()>=self.maxsize:
            print ("stack")
        else:
            self.stack.append(data)
            print (self.stack)
    def pop(self):
        if self.size()<=0:
            print ("stack Empty")
        else:
            self.stack.pop()
            print (self.stack)
    def peek(self):
        return self.stack[len(self.stack)-1]
    def size(self):
        return len(self.stack)

s=stack()
print("ตรวจสอบคำว่าแสตกว่างหรือไม่ =",s.isEmpty())
print("การนำเข้าข้อมูลไปในแสตก")
s.push(5)
s.push(10)
s.push(15)
s.push(20)
s.push(25)
s.push(30)
print ("คืนค่าข้อมูลตัวสุดท้าย =",s.peek())
print ("จำนวนข้อมูล =",s.size())
print ("ตรวจสอบว่าว่างไหม =",s.isEmpty())
print("การนำข้อมูลออกจากแสตก")
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
print("จำนวนของข้อมูล =",s.size())
