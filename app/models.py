from enum import unique
from app import db

class Product(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    product_name=db.Column(db.String(50),nullable=False, unique=True)
    price=db.Column(db.Float(),nullable=False)
    image=db.Column(db.String())

    def __init__(self,product_name,price,image):
        self.product_name=product_name
        self.price=price
        self.image=image