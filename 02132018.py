class HashTable:
    def __init__(self):
        self.size = 2
        self.slots = [None]*self.size
        self.data=[None]*self.size
    def put(self, key, data):
        hash_value = self.hash_function(key,len(self.slots))
        if self.slots[hash_value] == None:
            self.slots[hash_value]=key
            self.data[hash_value]=data
        else:
            if self.slots[hash_value] ==key:
                self.data[hash_value]=data
            else:
                next_slot=self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and \
                      self.slots[next_slot] != key:
                    next_slot=self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] ==None:
                    self.slots[next_slot]=key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot]=data
    def hash_function(self, key, size):
        return key % size
    def rehash(self, old_hash, size):
        return (old_hash +1) % size
    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data=None
        stop=False
        found=False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position]==key:
                found=True
                data=self.data[position]
            else:
                psition=self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop=True
        return data
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, data):
        self.put(key, data)
        

print( "Hello")
password=""
attempt=0
flag=0
while(attempt!=3):
    password = input("Enter Password ")
    if(password=="1234"):
        flag=1
        break
    else:
        attempt=attempt+1
        if(attempt==3):
            print("You are blocked for a while")
            exit()

h=HashTable()
user = input('Type your score ')
if user.isdigit():
    user1=int(user)
    if (user1 >=90):
        if (user1 > 100):
            print("Try again")
        
        else:
            h[000]="Code: Summa Cum Laude"
            h[100]="Amazing Student!"
            print ("A")   
            
    elif (user1 >=80):
        h[221]="Code: Magna Cum Laude"
        h[222]="Excellent Student!"
        
        print ("B")
        
    elif (user1 >=70):
        h[300]="Cum Laude"
        h[333]="Great Student!"
        print ("C")
        
    elif (user1 >=60):
        h[444]="Laude"
        h[400]="Nice Student!"
        print ("D")
        
    else:
        if (user1 <0):
            print("Negative impossible")
            
        else:
            h[500]="TORALLY FAILED"
            h[555]="TAKE THIS AGAIN"
            print ("F")
            
else:
    print("INTEGER ONLY")
    h[999]="Error Code Detected"
    h[998]="Invalid"

print (h.slots)
print (h.data)


    


    
    
    
  


