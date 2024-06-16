#Importing all required libraries
from app import db
import uuid

class Products(db.Model):#A class for storing all product details
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String(64))
    image = db.Column(db.String(128))
    rating = db.Column(db.Integer)
    marked_price = db.Column(db.Float)
    selling_price = db.Column(db.Float)

    @staticmethod
    def create(name, image, rating, marked_price, selling_price):#To generate new product details
        product_dict = dict(
            guid = str(uuid.uuid4()),
            name = name,
            image = image,
            rating = rating,
            marked_price = marked_price,
            selling_price = selling_price
        )
        #Below code to push product details into class Products
        product_obj = Products(**product_dict)
        db.session.add(product_obj)
        db.session.commit()

    def update(self, **details_dict):#To update order details if required
        for k,v in details_dict.items():
            setattr(self, k, v)
        db.session.commit()