from Room import Room
from building import Building
from subject import Subject
from lecturer import Lecturer
from student import Student

s01 = Student("6814931020", "Michel Tonog")

r438 = Room("438")
r436 = Room("436")
r434 = Room("434")
r35408 = Room("35408")

b4 = Building("4")
b35 = Building("35")

sub9043042 = Subject("9043042-55","Standards in Geoinformatics",3)
sub9042051 = Subject("9042051-55","Object-Oriented Programming for Geoinformatics",3)
sub9043041 = Subject("9043041-59","Spatial Analysis and Modeling",3)
sub0265011 = Subject("0265011-65","Digital Literacy for Innovator",3)
sub9042052 = Subject("9042052-59","Advanced Web Programming",3)
sub9042041 = Subject("9042041-55","Database Management in Geographic Information Systems",3)

l1 = Lecturer("อาจารย์ภูมิพัฒน์ อุ่นบ้าน")
l2 = Lecturer("อาจารย์นิทัศน์ นิลฉวี")
l3 = Lecturer("ผู้ช่วยศาสตราจารย์วิระ ศรีมาลา")
l4 = Lecturer("ผู้ช่วยศาสตราจารย์ ดร. ภูวดล บัวบางพลู")

print(s01)
print(r438)
print(r436)
print(r434)
print(r35408)
print(b4)
print(b35)
print(sub9043042)
print(sub9042051)
print(sub9043041)
print(sub0265011)
print(sub9042052)
print(sub9042041)
print(l1)
print(l2)
print(l3)
print(l4)