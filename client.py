from user import user

class client(user):
    def __init__(self,id=None,email=None, password=None,type="CLIENT", name=None,aemail=None, gender=None, no_order=None,p_pic=None,bg_pic=None):
        super().__init__(id,email, password,type)
        self.name=name
        self.email=aemail
        self.gender=gender
        self.no_orders = no_order
        self.p_pic=p_pic
        self.bg_pic=bg_pic
