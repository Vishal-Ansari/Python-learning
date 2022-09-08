class Dad:
    basketball=2


class son(Dad):
    dance=1
    def isdance(self):
        return f"yes i can dance {self.dance} no of times"


class Grandson(son):
    dance=7
    def isdance(self):
        return f"ohh yeaa m to mst nachta hu {self.dance} trh s"

dady=Dad()        
sony=son()
pota=Grandson()


print(pota.isdance())
print(pota.basketball)