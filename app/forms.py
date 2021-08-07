from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class Create_product(FlaskForm):
        product_name = StringField('Product Name', validators=[DataRequired()])
        price = StringField('Product Price', validators=[DataRequired()])
        image = TextAreaField('Image URL')
        submit = SubmitField()