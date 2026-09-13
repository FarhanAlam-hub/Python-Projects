class employee:
    a = 1 #  ---> Class attr
    @classmethod # ---> By using this we can print class attr even if instance attr is present. 
    def show(cls):
        print(f"The class vlaue is:{cls.a}")

e = employee()
e.a =54 # ---> Instance attr
e.show()

