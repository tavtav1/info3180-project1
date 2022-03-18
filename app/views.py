"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from app.forms import PropertyForm
from app.models import PropertyInfo
from werkzeug.utils import secure_filename 


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['GET','POST'])
def create():
    #Instantiate form class
    form = PropertyForm()

    if form.validate_on_submit():

        property_title = form.title.data
        description = form.description.data
        no_of_bedrooms = form.bedrooms.data
        no_of_bathrooms = form.bathrooms.data
        price = form.price.data
        property_type = form.ptype.data
        loc = form.location.data

        #Getting file name
        f = form.photo.data
        filename = secure_filename(f.filename)
 

        #Saving file to folder
        image = request.files["photo"]
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename))
        image.save(file_path)

        

        #Adding to Database
        user = PropertyInfo(property_title, description, no_of_bedrooms, no_of_bathrooms, price, property_type, loc, photo_name=filename)
        db.session.add(user)
        db.session.commit()

        flash('Property Added Successfully')
        return redirect(url_for('properties'))

    return render_template('create.html', form = form)


@app.route('/properties/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)
    

@app.route('/properties')
def properties():
    propertiespost = PropertyInfo.query.order_by(PropertyInfo.property_title)
    return render_template('properties.html', propertiespost = propertiespost)

@app.route('/properties/<int:propertyid>')
def property(propertyid):
    propertypost = PropertyInfo.query.get_or_404(propertyid)
    return render_template('property.html', propertypost = propertypost)




@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
