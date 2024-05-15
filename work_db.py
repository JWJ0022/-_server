import db_setup

def register_building(session,db,Building,building_name):
    building_name = request.form['building_name']

    building = Building.query.filter_by(name=building_name).first()

    if not building:
        building = Building(name=building_name)
        db.session.add(building)
        db.session.commit()

    session['building_id'] = building.id
    return "building registered successfully", 201

def save_to_db(latitude, longitude, altitude, s3_url):
    wall_id = session.get('wall_id')

    new_data = DroneData(
        wall_id = wall_id,
        latitude=latitude,
        longitude=longitude,
        altitude=altitude,
        s3_url=s3_url,
    )
    db.session.add(new_data)
    db.session.commit()


@app.route('/register_wall', methods=['POST'])
# building_id, direction
def register_wall(session, db, Wall, direction):
    building_id = session.get('building_id')

    direction = request.form['direction']

    wall = Wall.query.filter_by(direction=direction, building_id=building_id).first()
    if not wall:
        wall = Wall(direction=direction, building_id=building_id)
        db.session.add(wall)
        db.session.commit()

    session['wall_id'] = wall.id
    return "Wall registered successfully", 201