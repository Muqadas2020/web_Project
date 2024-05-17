from user import user

class artist(user):
    def __init__(self,id=None,email=None, password=None,type="ARTIST", name=None,bname=None,aemail=None, gender=None,des=None,job=None,no_p=None,p_pic=None,bg_pic=None):
        super().__init__(id,email, password,type)
        self.name=name
        self.bname=bname
        self.email=aemail
        self.gender=gender
        self.description=des
        self.job=job
        self.no_projects = no_p
        self.p_pic=p_pic
        self.bg_pic=bg_pic
