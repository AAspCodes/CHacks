from flask import render_template, url_for, flash, redirect
from Website import app, db
from Website.forms import RegistrationFrom
from Website.models import Subscriber

@app.route("/", methods=['GET','POST'])
def home():
    form = RegistrationFrom()
    if form.validate_on_submit():
        print('form valid')
        subscriber = Subscriber(email=form.email.data,
                                everett=form.everett.data,
                                skagit_county=form.skagit_county.data,
                                weather=form.weather.data,
                                sports=form.sports.data)
        db.session.add(subscriber)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in.',
              'success')
        return redirect(url_for('home'))

    else:
        print('form not valid')


    return render_template("home.html", form=form)