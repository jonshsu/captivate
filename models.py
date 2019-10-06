from app import db

class SpreadsheetData(db.Model):
    __tablename__ = "spreadsheetdata"
    
    id = db.Column(db.Integer, primary_key=True)
    mydata = db.Column(db.Text())

    def __init__ (self, mydata):
        self.mydata = mydata