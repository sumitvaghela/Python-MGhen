from flask import Flask, render_template
import urllib.request
import json
	

app = Flask(__name__)
	

	

@app.route('/')
def index():
	

    response        = urllib.urlopen('http://api.fixer.io/latest?base=AUD')
    data  = json.load(response)
	

    currencyunit_data         = data["base"]
    currencyunit_country           = data["currencyunit_country"]
    currencyunit_records = []
	

    for currencyunit in currencyunit_country_index:
	record_tuple = (currencyunit_country, currencyunit["date"], currencyunit["rates"])
	currencyunit_records.append(record_tuple)
	

    return render_template('index.html', records= currencyunit_records)
	

	

if __name__ == '__main__':
    # Starts the Flask application server
    app.run(debug=True)

