from app import app # from the app folder, import the app variable (Flask instance)
from flask import request, Flask, render_template, request, jsonify, redirect, url_for
from app.schemas.userSchema import user_input_schema, user_output_schema, users_schema
from app.schemas.budgetSchema import 
# from app.schemas.productSchema import product_schema, products_schema
from marshmallow import ValidationError
from app.database import db
from app.models import User, Budget
from werkzeug.security import generate_password_hash

@app.route('/')
def index():
    return 'filler statement'

# Get all customers
@app.route('/users', methods=['GET'])
def get_all_users():
    query = db.select(User)
    users = db.session.execute(query).all()
    return users_schema.jsonify(users)

#get a single customer by id
@app.route('/users/<int:user_id>' , methods=["GET"])
def get_single_user(user_id):
    #Search for a customer with ID
    user = db.session.get(User, user_id)
    # Check if we get a customer back or None
    if user is not None:
            return user_output_schema.jsonify(user)
    return{"error": f"User with ID {user_id} does not exist"}, 404 #not found


@app.route('/users', methods=["POST"])
def create_user():
    #Check if the request has a JSON body
    if not request.is_json:
        return{"error": "Request body must be application/json"}, 400 #Bad request by client
    try:
        #Get the request JSON body
        data = request.json
        # check if the body has all the required fields
        user_data = user_input_schema.load(data)
        #Query the customer table to see if any customers have that username or email
        query = db.select(User).where( (User.username == user_data['username']) | (User.email == user_data['email']) )
        check_users = db.session.scalars(query).all()
        if check_users: # if there are customers in the check_customers list (empty list evaluatea to false)
             return {"error": "User with that username and/or email already exists"}, 400 #Bad request by Client
        #Create a new instance of Customer and add to the database
        new_user = User(
             first_name=user_data['first_name'],
             last_name=user_data['last_name'],
             username=user_data['username'],
             email=user_data['email'],
             password=generate_password_hash(user_data['password'])
        )
        #and add to the database
        db.session.add(new_user)
        db.session.commit()
       
        user_data["id"] = len(users) + 1
        users.append(user_data)
        return user_output_schema.jsonify(new_user), 201 #created - Success
    except ValidationError as err:
        return err.messgaes, 400
    except ValueError as err:
         return {"error": str(err)}, 400



# app = Flask(__name__)
# app.config.from_object('config.Config')

# db.init_app(app)

# @app.route('/')
# def index():
#     transactions = Transaction.query.all()
#     budgets = Budget.query.all()
#     return render_template('index.html', transactions=transactions, budgets=budgets)

# @app.route('/add_transaction', methods=['GET', 'POST'])
# def add_transaction():
#     if request.method == 'POST':
#         amount = float(request.form['amount'])
#         category = request.form['category']
#         trans_type = request.form['type']
#         date = datetime.datetime.strptime(request.form['date'], '%Y-%m-%d')

#         transaction = Transaction(amount=amount, category=category, type=trans_type, date=date)
#         db.session.add(transaction)
#         db.session.commit()
#         return redirect(url_for('index'))
    
#     return render_template('add_transaction.html')

# @app.route('/add_budget', methods=['GET', 'POST'])
# def add_budget():
#     if request.method == 'POST':
#         category = request.form['category']
#         amount = float(request.form['amount'])
#         month = request.form['month']

#         budget = Budget(category=category, amount=amount, month=month)
#         db.session.add(budget)
#         db.session.commit()
#         return redirect(url_for('index'))
    
#     return render_template('add_budget.html')

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)
