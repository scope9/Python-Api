# jsonify is used to create a json response
from flask import Flask, request, jsonify

# create flask application. Double underscore is called Dunder method
app = Flask(__name__)

# to make this accessible use a decorater so we type @ symbol + name of our flask application in this case app. The slash / is the default route and whatever is after the slash is the url address bar. By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
# @app.route("/")
# # to create a route need to define a python function in this case home
# def home():
#     # return data to users when they reach this root
#     return "Home"

#GET Request
# Pass a path parameter <user_id> which is a dynamic value that you can pass in the path of a url that can access inside of route. For example if I put this in the url "/get-user/6226" then I retrieve this userid information which in this mock data is name and email
@app.route("/get-user/<user_id>")
# Make function and accept a variable inside the parameter thats the same as path parameter which is user_id.
def get_user(user_id):
    # Mock Data
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    # query parameter is an extra value that is included after the main path. Ex: "get-user/123?extra=hello world" After? you can pass different query parameter so something like extra is an additional key value you can pass in route
    # this is how to do the query parameter in flask. In this code request is the variable we imported, args stores all query parameter in a dictionary, then .get to access a value like extra
    extra = request.args.get("extra")
    # check if extra exist
    if extra:
        user_data["extra"] = extra
    # return data with a response code of 200. Jsonify is what we imported. Whenver we return data from an api we use json(javascript object notation) which is a key value pairs very similar to python dictionary. So in flask we create that dictionary "name": "John Doe" and jsonify it to return to the user allowing flask to parse this value returning as json data
    return jsonify(user_data), 200

#POST Request
#Since we're not using the default get request we specify the method for this route
@app.route("/create-user", methods=["POST"])
def create_user():
# gives all json data passed in the body of the request
    data = request.get_json()
# return this data back to the user to indicate it was created successfully 
    return jsonify(data), 201
# run flask application server
if __name__ == "__main__":
    app.run(debug=True)