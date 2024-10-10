from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random


app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        my_dict = {}
        for column in self.__table__.columns:
            my_dict[column.name] = getattr(self, column.name)
        return my_dict


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search")
def get_cafe():
    query_location = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location==query_location))
    selected_cafes = result.scalars().all()
    if selected_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in selected_cafes])
    else:
        return jsonify({"error": "Sorry you don't have a cafe at that location!"})

## HTTP POST - Create Record
@app.route("/add", methods=['GET', 'POST'])
def add():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_sockets=bool(request.form.get('has_sockets')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=request.form.get('coffee_price'),
        )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe. "})

## HTTP PUT/PATCH - Update Record
@app.route('/update/<int:id>', methods=['PATCH'])
def update(id):
    query_price = request.args.get('new_price')
    selected_cafe = db.get_or_404(Cafe, id)
    if selected_cafe:
        selected_cafe.coffee_price = query_price
        db.session.commit()
        return jsonify(response={"Success": "Successfully updated the price. "}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404
    
## HTTP DELETE - Delete Record
@app.route("/report_deleted/<int:id>", methods=['DELETE'])
def old_cafe(id):
    user_api_key = request.args.get('api_key')
    selected_cafe = db.get_or_404(Cafe, id)
    if selected_cafe:
        if user_api_key == 'TopSecretApiKey':
            db.session.delete(selected_cafe)
            db.session.commit()
            return jsonify(response={"Success": "Successfully deleted the cafe. "}), 200
        else:
            return jsonify(error={'Not Found': "Sorry that's not allowed. Make sure you have the correct api key."}), 403
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404

if __name__ == '__main__':
    app.run(debug=True)
