import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
import requests
from sqlalchemy.sql.expression import false
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, found, indexing
from re import sub
from decimal import Decimal
import math

# Manual environment Variables
from dotenv import * 
load_dotenv()


class PageResult:
   def __init__(self, data, page = 1, number = 20):
     self.__dict__ = dict(zip(['data', 'page', 'number'], [data, int(page), number]))
     self.full_listing = [self.data[i:i+number] for i in range(0, len(self.data), number)]
   def __iter__(self):
     for i in self.full_listing[self.page-1]:
       yield i
   def __repr__(self): #used for page linking
     return "/history/{}".format(self.page+1) #view the next page

# Global variable for easier search
global allsymbols

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    
    # Retrieve all symbols in case of page refresh at Index
    global allsymbols
    
    # Create a variable for the total
    total = 0
    # Get user's Cash
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session.get("user_id"))[0]["cash"]

    # Get user bought Stocks
    stocks = db.execute("SELECT stock_symbol, shares, price FROM stocks WHERE user_id = ? AND shares > 0", session["user_id"])

    # Prepare table
    if stocks:
        table = indexing(stocks, True)
    else:
        table=[]

    # Calculate total
    total += cash
    # Loop through table
    for item in table:
        # Get the total value of each row
        money = item["total"]

        # Convert it to Decimal point using regular expression (I think)
        value = float(sub(r'[^\d\-.]', '', money))

        # Add it to total
        total+=value

    # Render Index
    return render_template("index.html", cash=usd(cash), total=usd(total), table=table)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        # Get the hidden value to check which form is being submitted
        answer = request.form.get("buy")

        # If search form is submitted
        if answer == "search":
            # Get the symbol/name.
            search = request.form.get("symbol").upper()

            # Pass symbol to the found function, along with all the symbols for searching
            data = found(search, allsymbols)

            # If it wasn't found by name, try searching for it through symbol only.
            if not data:
                data = lookup(request.form.get("symbol"))
            
            # if found, render the buy html page with a new table, and clear the symbol text field
            if data != None:
                return render_template("buy.html", table=data, symbol = "")
            
            # If not found, tell user stock was not found through a danger alert.
            else:
                flash("Stock not found: Double check Symbol/Name.")
                return render_template("buy.html", symbol = search, type="danger")
        
        # If the user submitted the buy form
        elif answer == "buy":
            
            # Get all the table symbols.
            symbols = request.form.getlist("TSymbol")
            
            # Start an empty list to check for which symbols the user is buying
            buying = dict()
            keys = []

            # loop through the list of symbols
            for symbol in symbols:
                # Try and get the input field corresponding to such symbol
                stock = request.form.get(symbol)
                
                # If it is empty or 0, continue looking
                if not stock or stock == "0":
                    continue
                
                # Else, append the symbol as well as the number given in check.
                else:
                    buying[symbol] = stock
                    keys.append(symbol)
            # If the user is buying stuff
            if buying:
                # First join all stocks he is buying and look up their current information
                stocks = lookup(",".join(keys))

                # Create empty lists for successful transactions and failed transactions
                noMoney = []
                success = []
                # Get the cash of the user
                cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
                cash = float(cash[0]["cash"])

                # Loop through current information on stocks the user wants to buy
                for item in stocks:
                    total = round(float(buying[item["symbol"]]) * float(item["price"]), 2)
                    if cash > total:
                        # Check if the user has bought some of these stocks before.
                        check = db.execute("SELECT * FROM stocks WHERE user_id = ? AND stock_symbol = ?", session["user_id"], item["symbol"])

                        # If They have, store it in a variable that says its already there in the database
                        if check:
                            # Give user the stocks and subtract money from the user
                            db.execute("UPDATE stocks SET shares = shares + ?, price = ? WHERE user_id = ? AND stock_symbol = ?", buying[item["symbol"]], item["price"], session["user_id"], item["symbol"])
                            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - total, session["user_id"])
                            cash -= total
                            # Get order ID and Add that order to the history table
                            orderid = db.execute("SELECT order_id FROM stocks WHERE user_id = ? AND stock_symbol = ?", session["user_id"], item["symbol"])
                            db.execute("INSERT INTO history (user_id, stock_change, order_id, price) VALUES (?,?,?,?)", session["user_id"], buying[item["symbol"]], orderid[0]["order_id"], item["price"])

                        # If its not there, store it in a list that says its not there
                        else:
                            # Add the new stock into the stocks table and link it to user, then subtract money
                            db.execute("INSERT INTO stocks (user_id, stock_symbol, stock_name, shares, price) VALUES (?, ?, ?, ?, ?)", session["user_id"], item["symbol"], item["name"], buying[item["symbol"]], item["price"])
                            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - total, session["user_id"])
                            cash -= total

                            # Add the purchase to history
                            orderid = db.execute("SELECT order_id FROM stocks WHERE user_id = ? AND stock_symbol = ?", session["user_id"], item["symbol"])
                            db.execute("INSERT INTO history (user_id, stock_change, order_id, price) VALUES (?,?,?,?)", session["user_id"], buying[item["symbol"]], orderid[0]["order_id"], item["price"])
                        
                        # Add this to successful orders for user feedback
                        success.append([item["symbol"], buying[item["symbol"]], total])
                    # If the user has no money, add it to noMoney list for user feedback.
                    else:
                        noMoney.append([item["symbol"], buying[item["symbol"]], total])
                
                
                # If there are successful purchases
                if success:
                    # Start a string to concatenate later
                    userfeedback = "The following transactions have Succeeded: "
                    
                    # Loop through items in the successful purchases list
                    for item in success:
                        # Concatenate these purchases in the successful purchases message. and tell the user those purchases have been completed.
                        userfeedback = userfeedback + str(item[0]) + ". Number of Stocks: " + str(item[1]) + ". Price: " + usd(item[2]) + " - "
                    userfeedback += "Purchase Complete!"

                    # Add the message to flash to use as an alert.
                    flash(userfeedback)

                # Do the same for no money, giving user appropriate feedback.
                if noMoney:
                    userfeedbackfail = "The following Transactions Have failed: "
                    for item in noMoney:
                        userfeedbackfail = userfeedbackfail + item[0] + ". Number of Stocks: " + item[1] + ". Price: " + usd(item[2]) + " - "
                    userfeedbackfail += "Reason: No Cash."
                    flash(userfeedbackfail)
                
                # Refresh the page with new feedback alerts.
                return render_template("buy.html", type="primary")
            else:
                flash("No stocks Chosen")
                return render_template("buy.html", type="primary")
        else:
            return apology("Something wrong with buy if else statement.")


@app.route("/history/<pagenum>")
@login_required
def history(pagenum):
    """Show history of transactions"""
    # Get the history of the user
    history = db.execute("SELECT * FROM history WHERE user_id = ? ORDER BY date DESC", session["user_id"])
    if history:
        # Prepare a neat list of things the user will see
        mainHistory = []
        
        # Loop through history
        for item in history:
            # Get all information about the order from main table
            check = db.execute("SELECT * FROM stocks WHERE order_id = ?", item["order_id"])[0]
            # Prepare neat table to show
            mainHistory.append({
                "symbol" : check["stock_symbol"],
                "name" : check["stock_name"],
                "shares" : item["stock_change"],
                "price" : item["price"],
                "date" : item["date"]
            })

        # Items per page
        items_per_page = 20
        
        # How many pages
        length = math.ceil(len(mainHistory) / items_per_page)
        
        # Render Page
        return render_template("history.html", table = PageResult(mainHistory, pagenum), length = length)
    else:
        return render_template("history.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("Username/Password Are incorrect")
            username = request.form.get("username")
            return render_template("login.html", type="danger", username=username)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        
        # Retrieve all symbols once for later use.
        global allsymbols
        allsymbols =  pd.read_csv(r"AllSymbols.csv").to_dict('records')

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    global allsymbols
    # If requested through get, display it
    if request.method == "GET":
        return render_template("quote.html")

    # If requested through Post
    else:
        # Retrieve user input in all caps
        userSymbol = request.form.get("symbol").upper()
        
        data = found(userSymbol, allsymbols)
           
        if not data:
            # if not found, try looking up user input directly
            data = lookup(request.form.get("symbol"))
        
        # If data is received, update page with given data
        if data != None:
            return render_template("quote.html", table=data)
        # If stock not found, tell user.
        else:
            flash("Stock not found: Make sure the symbol is correct")
            return render_template("quote.html", type="danger")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # if called through GET, display form
    if request.method == "GET":
        return render_template("register.html")
    # If called through post
    else:
        # Check if username is taken
        if len(db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))) != 0:
            # If username is taken, tell user, clear form
            flash("Username Already Registered")
            return render_template("register.html", type="warning", username=request.form.get("username"))
        
        # Check if passwords match
        elif request.form.get("password") != request.form.get("Cpassword"):
            # If passwords don't match, tell user, clear form
            flash("Passwords do not match")
            return render_template("register.html", type="danger")
        
        # If username is new and passwords match
        else:
            # Add user to database and make sure to Hash their password
            db.execute("INSERT INTO users (username, hash) VALUES (?,?)", request.form.get("username"), generate_password_hash(request.form.get("password")))
            
            # Tell user the registration was successful
            flash("Registration Successful")

            # Redirect to login page.
            return render_template("login.html", type="success")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        # Get user bought Stocks
        stocks = db.execute("SELECT stock_symbol, shares, price FROM stocks WHERE user_id = ? AND shares > 0", session["user_id"])
        

        # Prepare table
        if stocks:
            table = indexing(stocks, True)
        else:
            table=[]
        
        return render_template("sell.html", table=table)
    else:
        # Get all the table symbols.
        symbols = request.form.getlist("TSymbol")

        # Start an empty list to check for which symbols the user is selling
        selling = dict()
        keys = []

        # loop through the list of symbols
        for symbol in symbols:
            # Try and get the input field corresponding to such symbol
            stock = request.form.get(symbol)
            
            # If it is empty or 0, continue looking
            if not stock or stock == "0":
                continue
            
            # Else, append the symbol as well as the number given in check.
            else:
                selling[symbol] = stock
                keys.append(symbol)
        # If the user is selling
        if selling:
            # Get user bought Stocks
            UserStocks = db.execute("SELECT stock_symbol, shares, price FROM stocks WHERE user_id = ? AND shares > 0", session["user_id"])

            # Get a net table of all the users owned stocks, not converted to USD
            table = indexing(UserStocks, False)

            # Empty lists for user feedback
            success = []
            failed = []

            # Loop through the table
            for item in table:
                # If you find an item that the user wants to sell
                if item["symbol"] in keys:
                    # Check if the user has the shares to sell
                    if int(item["shares"]) >= int(selling[item["symbol"]]):
                        # if he does, get the total amount of money he will receive
                        total = round(float(item["priceC"]) * float(selling[item["symbol"]]), 2)

                        # Get the order ID
                        orderid = db.execute("SELECT order_id FROM stocks WHERE stock_symbol = ? AND user_id = ?", item["symbol"], session["user_id"])

                        # Update stocks and subtract the number of shares the user sold
                        db.execute("UPDATE stocks SET shares = shares - ? WHERE user_id = ? AND order_id = ?", int(selling[item["symbol"]]), session["user_id"], orderid[0]["order_id"])

                        # Give money to the user
                        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total, session["user_id"])

                        # Add transaction to history and make it successful
                        db.execute("INSERT INTO history (user_id, stock_change, order_id, price) VALUES (?,?,?,?)", session["user_id"], -int(selling[item["symbol"]]), orderid[0]["order_id"], item["priceC"])
                        success.append([item["symbol"], selling[item["symbol"]], total])
                    # If the user does not have enough stocks, add it to failed transactions
                    else:
                        failed.append([item["symbol"], selling[item["symbol"]]])
            # If there are successful purchases
            if success:
                # Start a string to concatenate later
                userfeedback = "The following transactions have Succeeded: "
                
                # Loop through items in the successful purchases list
                for item in success:
                    # Concatenate these purchases in the successful purchases message. and tell the user those purchases have been completed.
                    userfeedback = userfeedback + item[0] + ". Number of Stocks: " + item[1] + ". Price: " + usd(item[2]) + " - "
                userfeedback += "Sale Complete!"

                # Add the message to flash to use as an alert.
                flash(userfeedback)

            # Do the same for no money, giving user appropriate feedback.
            if failed:
                userfeedbackfail = "The following Transactions Have failed: "
                for item in failed:
                    userfeedbackfail = userfeedbackfail + item[0] + ". Number of Stocks: " + item[1] + " - "
                userfeedbackfail += "Reason: Not enough owned stocks"
                flash(userfeedbackfail)

            UserStocks = db.execute("SELECT stock_symbol, shares, price FROM stocks WHERE user_id = ? AND shares > 0", session["user_id"])
            if UserStocks:
                table = indexing(UserStocks, True)
            else:
                table = []

            return render_template("sell.html", type="primary", table=table)
        else:
            flash("Please select at least 1 stock to sell")
            UserStocks = db.execute("SELECT stock_symbol, shares, price FROM stocks WHERE user_id = ? AND shares > 0", session["user_id"])
            if UserStocks:
                table = indexing(UserStocks, True)
            else:
                table = []
            return render_template("sell.html", type="primary", table=table)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

