from flask import Flask, request, jsonify
import mysql.connector

# initialize the flask application
app = Flask(__name__)

# Create database connection
conn = mysql.connector.connect(
    host="roundhouse.proxy.rlwy.net",
    user="root",
    password="aCa4-GehdH31BGHe1fDh4H4hagdC1hD5",
    database="railway",
    port=14241
)

mycursor = conn.cursor()


@app.route('/insert_location', methods=['POST'])
def insert_location():
    try:
        tenant_name = request.form.get('tenantName')
        premises_address = request.form.get('premiseAddress')
        contact_person = request.form.get('contactPerson')
        inspector_name = request.form.get('inspectorName')
        inspection_date = request.form.get('inspectorDate')
        contact_number = request.form.get('contactNumber')

        sql = ("INSERT INTO locations (tenant_name, premise_address, contact_person, "
               "contact_number, inspection_date, Inspector_name) "
               "VALUES (%s, %s, %s, %s, %s, %s)")
        val = (tenant_name, premises_address, contact_person, contact_number, inspection_date, inspector_name)

        mycursor.execute(sql, val)
        conn.commit()
        return jsonify({'message': 'location inserted successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/insert_inverter', methods=['POST'])
def insert_inverter():
    try:
        qr_code = request.form.get('qrCode')
        inverter_manufacturer = request.form.get('inverterManufacture')
        inverter_capacity = int(request.form.get('inverterCapacity'))
        serial_number = request.form.get('inverterSerial')
        installation_date = request.form.get('installationDate')

        battery_manufacturer = request.form.get('batteryManufacture')
        battery_type = request.form.get('batteryType')
        battery_serial = request.form.get('batterySerial')
        battery_capacity = int(request.form.get('batteryCapacity'))
        num_of_batteries = int(request.form.get('numOfBatteries'))

        sql = ("INSERT INTO inverters (qr_code, inverter_manufacturer, inverter_capacity, serial_number, "
               "installation_date, battery_manufacturer, battery_type, battery_capacity, num_of_batteries,"
               " battery_serial) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        val = (qr_code, inverter_manufacturer, inverter_capacity, serial_number, installation_date,
               battery_manufacturer, battery_type, battery_capacity, num_of_batteries, battery_serial
               )

        mycursor.execute(sql, val)
        conn.commit()
        return jsonify({'message': 'inverter inserted successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
