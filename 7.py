# multi inheritance
class grandparent:
    def show1(self):
        print("grandparent")


class parent(grandparent):
    def show2(self):
        print("parent")
class child(parent):
    pass
g1=grandparent()
g1.show1()



p1=parent()
p2.show1()
             





c1=child()
c1.show2()        