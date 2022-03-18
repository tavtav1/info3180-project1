from . import db

class PropertyInfo(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'property_info'

    id = db.Column(db.Integer, primary_key=True)
    property_title = db.Column(db.String(150))
    description = db.Column(db.String(300))
    no_of_bedrooms = db.Column(db.String(80))
    no_of_bathrooms = db.Column(db.String(80))
    price = db.Column(db.String(80))
    property_type = db.Column(db.String(50))
    loc = db.Column(db.String(100))
    photo_name = db.Column(db.String(80))


    def __init__(self, property_title, description, no_of_bedrooms, no_of_bathrooms, price, property_type, loc, photo_name):
        self.property_title = property_title
        self.description = description
        self.no_of_bedrooms = no_of_bedrooms
        self.no_of_bathrooms = no_of_bathrooms
        self.price = price
        self.property_type = property_type
        self.loc = loc
        self.photo_name = photo_name
            

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.property_title)