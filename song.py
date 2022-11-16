import random
class SONG:
    def __init__(self,name,duration,frequency,next=None):
        self.name = name
        self.duration = duration
        self.frequency = frequency
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,name,duration,frequency):
        newsong = SONG(name,duration,frequency)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newsong
        else:
            self.head = newsong
            
    def printlist(self):
        current = self.head
        while current:
            print("song name ", current.name, "length of song is ", current.duration, "and the frequency is ", current.frequency)
            current = current.next
    def amount(self):
        current = self.head
        a = 0
        while current:
            a +=1
            current = current.next
        print(a)

    def searchsong(self):
        current = self.head
        name = input("")
        while current:
            if current.name == name:
                print("Found the song")
                print("playing ", current.name, "length of song is ", current.duration, "and the frequency is ", current.frequency)
                return True
            elif current.model != model:
                current = current.next
        print("Song was not found")
    
    def searchdelete(self):
        current = self.head
        song = input("what song are you looking to delete\n")
        while current:
            if current.name == song:
                print("Deleting ", current.name, "length of song is ", current.duration, "and the frequency is ", current.frequency)
                del(current.name,current.duration,current.frequency)
                return True
            elif current.name != song:
                current = current.next
        print("Song not found to delete")

song = LinkedList()
l = ''
num = int(input("how many songs would you like to add\n"))

for i in range(num):
    name = input("what is the name of the song\n")
    duration = input("How long is the song\n")
    frequency = input("What is the frequency\n")
    song.insert(name,duration,frequency)

while l != 'q':
    l = input("what would you like to do search for song(s), delete a song(d), or play the songs in order(p)")
    if l == 's':
        song.searchsong()
    if l == 'd':
        song.searchdelete()
    if l == 'p':
        song.printlist()
