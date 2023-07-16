import attr

@attr.s(auto_attribs=True)
class X:
    x: int

    def do(self):
        print(self.x)


x = X(1)
a = x.x