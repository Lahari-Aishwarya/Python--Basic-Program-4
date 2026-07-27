# single inheritance
class parent:
    def show(self):
        print("parent")
p1=parent()
p1.show()
class child(parent):
    pass
c1=child()
c1.show()        