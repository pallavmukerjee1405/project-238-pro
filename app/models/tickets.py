#Importing all required libraries
from app import db
import uuid

class Tickets(db.Model):#A class for storing all ticket details
    __tablename__ = "tickets"
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(64))
    description = db.Column(db.String(1024))
    attachment = db.Column(db.String(64))

    @staticmethod
    def create(user_id, title, description, attachment):#To generate new ticket details
        ticket_dict = dict(
            guid = str(uuid.uuid4()),
            user_id = user_id,
            title = title,
            description = description,
            attachment = attachment
        )
        #Below code to push ticket details into class Tickets
        ticket_obj = Tickets(**ticket_dict)
        db.session.add(ticket_obj)
        db.session.commit()

    def update(self, **details_dict):#To update ticket details if required
        for k,v in details_dict.items():
            setattr(self, k, v)
        db.session.commit()