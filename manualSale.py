from flask import Flask, request, render_template_string

app = Flask(__name__)

FORM_HTML = '''
<!doctype html>
<title>Enter Values</title>
<h1>Enter comma-separated values for each category</h1>
<form method="post">
  <label>Purchase (comma separated):</label><br>
  <input type="text" name="purchase" placeholder="e.g. 100,200,300"><br><br>

  <label>Sale (comma separated):</label><br>
  <input type="text" name="sale" placeholder="e.g. 150,250"><br><br>

  <label>PurchaseReturn (comma separated):</label><br>
  <input type="text" name="purchasereturn" placeholder="e.g. 50"><br><br>

  <label>SaleReturn (comma separated):</label><br>
  <input type="text" name="salereturn" placeholder="e.g. 30"><br><br>

  <input type="submit" value="Calculate">
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def calculate_totals():
    if request.method == 'POST':
        try:
            def parse_values(field):
                raw = request.form.get(field, "")
                # Split by comma, strip spaces, convert to float, ignore empty entries
                return [float(x.strip()) for x in raw.split(',') if x.strip()]

            purchase_vals = parse_values('purchase')
            sale_vals = parse_values('sale')
            purchasereturn_vals = parse_values('purchasereturn')
            salereturn_vals = parse_values('salereturn')

            total_purchase = sum(purchase_vals) - sum(purchasereturn_vals)
            total_sale = sum(sale_vals) - sum(salereturn_vals)

            result = f'''
            <h2>Results</h2>
            <p>Total Purchase = Sum(Purchase) - Sum(PurchaseReturn) = {sum(purchase_vals)} - {sum(purchasereturn_vals)} = <b>{total_purchase}</b></p>
            <p>Total Sale = Sum(Sale) - Sum(SaleReturn) = {sum(sale_vals)} - {sum(salereturn_vals)} = <b>{total_sale}</b></p>
            <br><a href="/">Try Again</a>
            '''
            return result
        except ValueError:
            return "Invalid input! Please enter numbers separated by commas.", 400

    return FORM_HTML


if __name__ == '__main__':
    app.run(debug=True)
