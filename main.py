from unicodedata import name

from paramiko import Agent


class Student:
    name=''
    age=20
    score=2.0 
    racks=["Java", "C#", "Python"]
    
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        # pass
        self.name=name
        self.age=age
        self.tracks=tracks
        self.score=score
        
        
    def change_name(self,name):
        self.name=name
        return self.name
        
    def change_age(self,age):
        self.age=age
        return self.age
    def add_track(self,tracks):
        
        self.tracks.append("lion")
        return self.tracks
    
    def get_score(self):
        
        return self.score
    
    
    



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score())
