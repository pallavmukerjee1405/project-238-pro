#Importing all required libraries
from app import db

from app.models.editor.customer import Customer

class CompanyOrders(db.Model):#A class for storing all company order details
    __tablename__ = "company_orders"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    total_amount = db.Column(db.Float)
    order_number = db.Column(db.Integer)

    @staticmethod
    def create(id, date, customer_id, total_amount, order_number):#To generate new company order details
        order_dict = dict(
            id = id,
            date = date,
            customer_id = customer_id,
            total_amount = total_amount,
            order_number = order_number
        )
        #Below code to push all company order details into class CompanyOrders
        order_obj = CompanyOrders(**order_dict)
        db.session.add(order_obj)
        db.session.commit()