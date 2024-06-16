#Importing all required libraries
from app import db

class Supplier(db.Model):#A class for storing all supplier details
    __tablename__ = "suppliers"
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(64))
    contact_name = db.Column(db.String(64))
    city = db.Column(db.String(64))
    country = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    fax = db.Column(db.String(64))

    @staticmethod
    def create(id, company_name, contact_name, city, country, phone, fax):#To generate new supplier details
        supplier_dict = dict(
            id = id,
            company_name = company_name,
            contact_name = contact_name,
            city = city,
            country = country,
            phone = phone
        )
        #Below code to push all supplier details into class Supplier
        supplier_obj = Supplier(**supplier_dict)
        db.session.add(supplier_obj)
        db.session.commit()