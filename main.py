# THE LECTURER'S COMPLETE SOLUTION IS SAVED WITHIN THE UPPER MAIN FOLDER...
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import csv

from AddCafeForm import AddCafeForm
from CafeDataClass import CafeDataClass

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
cafe_added = []

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


# @app.route('/add')
@app.route("/add", methods=['GET', 'POST'])
def add_cafe():
    form = AddCafeForm()
    if form.validate_on_submit():
        print("True")
        name = form.name.data
        location = form.location.data
        open = form.open.data
        close = form.close.data
        coffee = form.coffee.data
        wifi = form.wifi.data
        power = form.power.data
        cafe = CafeDataClass(name, location, open, close, coffee, wifi, power)
        cafe_added.append(cafe)

    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in list(csv_data):
            print(row)
            row_list = list(row)
            list_of_rows.append(CafeDataClass(row_list[0],
                                              row_list[1],
                                              row_list[2],
                                              row_list[3],
                                              row_list[4],
                                              row_list[5],
                                              row_list[6]))
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows + cafe_added)

if __name__ == '__main__':
    app.run(debug=True)
