class Area :
    def circle(self):
        rad = int(input("Enter the radius:"))
        area = (22/7)*(rad**2)
        print("Area is :" , area , "cm square")
        
        
    def square(self):
        side = int(input("Enter the length of a side:"))
        area = side**2
        print("Area is :" , area , "cm square")
        
    def rect(self):
        print("Enter length and breadth of rectangle:")
        le = int(input())
        br = int(input())
        area = le * br
        print("Area is :" , area , "cm square")
                   
    def cube(self):
        side = int(input("Enter length of a side:"))
        area = 6 * (side**2)
        print("Area is :" , area , "cm square")
                   
    def cuboid(self):
        print("Enter length , breadth and height :")
        le = int(input())
        br= int(input())
        he= int(input())
        area = 2*(le*br + br*he + he*le)
        print("Area is :" , area , "cm square")
                   
    def cylinder(self):
        rad = int(input("Enter the radius:"))
        he = int(input("Enter the height:"))
        area = (22/7)*(rad**2)*(he)
        print("Area is :" , area , "cm square")
        
        
shape = Area()

shape.circle()
shape.square()
shape.rect()
shape.cube()
shape.cuboid()
shape.cylinder()