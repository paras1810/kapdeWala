from flask import Flask, request, render_template_string
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

FORM_HTML = '''
<!doctype html>
<title>Enter Sales and Purchase Data</title>
<h1>Enter data for one date</h1>
<form method="post">
  <label>Date (MM/DD/YYYY):</label><br>
  <input type="text" name="date"><br><br>

  <label>Purchase values (comma-separated):</label><br>
  <input type="text" name="purchase"><br><br>

  <label>Sale values (comma-separated):</label><br>
  <input type="text" name="sale"><br><br>

  <label>PurchaseReturn values (comma-separated):</label><br>
  <input type="text" name="purchasereturn"><br><br>

  <label>SaleReturn values (comma-separated):</label><br>
  <input type="text" name="salereturn"><br><br>

  <input type="submit" value="Submit">
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Parse date input
            date_str = request.form['date'].strip()
            date_obj = datetime.strptime(date_str, '%m/%d/%Y')
            year = date_obj.year
            filename = f"{year}.xlsx"

            # Parse and sum all numeric fields
            def sum_field(name):
                raw = request.form.get(name, "")
                return sum(float(x.strip()) for x in raw.split(',') if x.strip())

            purchase_sum = sum_field('purchase')
            sale_sum = sum_field('sale')
            purchasereturn_sum = sum_field('purchasereturn')
            salereturn_sum = sum_field('salereturn')

            total_purchase = purchase_sum - purchasereturn_sum
            total_sale = sale_sum - salereturn_sum

            # Create new row
            new_data = pd.DataFrame([{
                'Date': date_obj.date(),
                'Total Purchase': total_purchase,
                'Total Sale': total_sale
            }])

            # If file exists, append; else create
            if os.path.exists(filename):
                existing_df = pd.read_excel(filename)
                combined_df = pd.concat([existing_df, new_data], ignore_index=True)
            else:
                combined_df = new_data

            # Save updated Excel
            combined_df.to_excel(filename, index=False)

            return f"<h3>Data written to <b>{filename}</b></h3><a href='/'>Enter More</a>"

        except Exception as e:
            return f"<b>Error:</b> {e}", 500

    return render_template_string(FORM_HTML)


if __name__ == '__main__':
    app.run(debug=True)
