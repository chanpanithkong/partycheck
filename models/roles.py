from config.db import db

class tbroles(db.Model):
    
    roleid = db.Column("roleid", db.Integer, primary_key = True)
    rolename = db.Column(db.String)
    details = db.Column(db.String)
    parentid = db.Column(db.Integer)
    
    def __init__(self, roleid=None,rolename=None,details=None,parentid=None):
        self.roleid = roleid
        self.rolename =rolename
        self.details = details
        self.parentid = parentid
        
    @classmethod
    def find_by_roleid(cls, roleid) -> "tbroles":
        return cls.query.filter_by(roleid=roleid).first()