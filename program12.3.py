class MyClass:
    def __init__(self):
        self.public_attribute="i'm a public attribute"
        self._protected_attribute="i'm a protected attribute"
        self._private_attribute="i'm a private attribute"
    def public_method(self):
        print("i'm a public method")
    def _protected_method(self):
        print("i'm a protected method")
    def _private_method(self):
        print("i'm a private method")
obj=MyClass()
print(obj.public_attribute)
obj.public_method()
print(obj._protected_attribute)
obj._protected_method()
print(obj._MyClass__private_attribute)
obj._MyClass__private_method()
