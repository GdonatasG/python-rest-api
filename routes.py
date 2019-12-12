from models.Car import Car
from models.CarSchema import CarSchema
from api import app, db
from flask import jsonify, make_response, request


@app.route('/cars')
def getAllCars():
    try:
        get_cars = Car.query.all()
        car_schema = CarSchema(many=True)
        cars = car_schema.dump(get_cars)
        return make_response(jsonify(cars))
    except:
        return make_response("No cars found!")


@app.route('/cars/<int:id>')
def getCarById(id):
    try:
        carObj = Car.query.filter_by(id=id).one()
        car_schema = CarSchema()
        cars = car_schema.dump(carObj)
        return make_response(jsonify(cars))
    except:
        return make_response("No cars found!")


@app.route('/cars/add', methods=['POST'])
def addCar():
    name = request.args.get('name')
    engine = request.args.get('engine')
    gas_type = request.args.get('gas_type')
    response = ""
    if name and engine and gas_type:
        new_car = Car(name=name, engine=engine, gas_type=gas_type)
        db.session.add(new_car)
        db.session.commit()
        response = make_response("Added!")
    else:
        response = make_response("Error while adding!")

    return response


@app.route('/cars/update/<int:id>', methods=['PUT'])
def updateCar(id):
    name = request.args.get('name')
    engine = request.args.get('engine')
    gas_type = request.args.get('gas_type')
    try:
        try:
            updated_car = Car.query.filter_by(id=id).one()
        except:
            raise TypeError
        if name and engine and gas_type:
            updated_car.name = name
            updated_car.engine = engine
            updated_car.gas_type = gas_type
            db.session.commit()
            db.session.flush()
            response = make_response("Updated!")
        else:
            raise TypeError
    except TypeError:
        response = make_response("Error while updating!")

    return response


@app.route('/cars/delete/<int:id>', methods=['DELETE'])
def deleteCar(id):
    try:
        car = Car.query.filter_by(id=id).one()
        db.session.delete(car)
        db.session.commit()
        response = make_response("Deleted!")
    except:
        response = make_response("Error while deleting!")

    return response


if __name__ == '__main__':
    app.run()
