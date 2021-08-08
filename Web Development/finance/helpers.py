import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://cloud.iexapis.com/stable/stock/market/batch?types=quote&symbols={urllib.parse.quote(symbol)}&range=5y%20&token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        Data = []
        for item in quote:
            item = quote[item]["quote"]
            Data.append({
            "name": item["companyName"],
            "price": float(item["latestPrice"]),
            "symbol": item["symbol"]
            })
        return Data
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


def found(userSymbol, allsymbols):
    # Look through all the symbols and find all matching, then convert them into a list
    found = list(filter(lambda symbol: userSymbol in symbol["name"], allsymbols))
        
    # If a list exists
    if found:
        # Temp variable to compile all data symbols
        DataSymbols = []

        # Loop through list
        for item in found:
            # Append the symbol only into datasymbols
            DataSymbols.append(item["symbol"])

        # After loop, Join all symbols with comma in between
        totalSymbols = ",".join(DataSymbols)

        # Send it to lookup to use the API
        data = lookup(totalSymbols)

        return data
    else:
        return None

def indexing(symbols, isUSD):
    # Prepare all symbols
    allsymbols = []
    
    # Loop through given list of dictionaries
    for item in symbols:
        # Get all the symbols
        allsymbols.append(item["stock_symbol"])
    # Look up corresponding quota
    data = lookup(",".join(allsymbols))
    # Prepare a table
    table = []
    # Loop through both symbols and quota
    for item1,item2 in zip(data,symbols):
        if isUSD:
            # Prepare an appropriate table
            table.append(
                {
                    "symbol" : item1["symbol"],
                    "name" : item1["name"],
                    "shares" : item2["shares"],
                    "priceB" : usd(item2["price"]),
                    "priceC" : usd(item1["price"]),
                    "total" : usd(item2["shares"] * item1["price"])
                }
            )
        else:
            # Prepare an appropriate table
            table.append(
                {
                    "symbol" : item1["symbol"],
                    "name" : item1["name"],
                    "shares" : item2["shares"],
                    "priceB" : item2["price"],
                    "priceC" : item1["price"],
                    "total" : item2["shares"] * item1["price"]
                }
            )
    # Return the table.
    return table