from flask import Flask,jsonify

app = Flask(__name__)

#Celsius
@app.route('/cel/<float:cel>')
def celsius(cel):
    fahrenheit=(cel*9/5)+32
    return jsonify({"Fahrenheit":fahrenheit})

#Fahrenheit
@app.route('/fah/<float:fah>')
def fahren(fah):
    celsius=(fah-32)*5/9
    return jsonify({'Celsius':celsius})

#trying both celsius and fahrenheit
@app.route('/')
def temp():
    print("1.convert to Fahrenheit \n2.convert to Celsius")
    temperature=int(input())
    if temperature == 1:
        celsius=float(input("enter the temperature in celsius:"))
        fahrenheit=(celsius*9/5)+32
        return jsonify({'Fahrenheit':fahrenheit})
    elif temperature == 2:
        Fahrenheit=float(input("enter the temperature in fahrenheit:"))
        Celsius=(Fahrenheit-32)*5/9
        return jsonify({'Celsius':Celsius})
    else:
        return jsonify({'message':'invalid statement'})

if __name__ == '__main__':
    app.run()
