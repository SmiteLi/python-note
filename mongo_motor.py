# $ pip install motor
import motor

client = client = motor.motor_tornado.MotorClient(
    "mongodb+srv://<username>:<password>@<cluster-url>/test?retryWrites=true&w=majority")
db = client.test
