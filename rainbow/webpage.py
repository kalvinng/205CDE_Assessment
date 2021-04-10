from flask import Flask, render_template, request, flash, redirect, url_for, session
from forms import SignUp, LoginPage, Admin_Account, Admin_EditPage, Admin_Product
import pymysql

app = Flask(__name__)
app.secret_key = 'bdd47e32d3cb98b57f15dedc'
app.jinja_env.globals.update(zip=zip, type=type, len=len)

def fetch_items(table, column):
    db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
    cursor = db.cursor()
    #sql command
    cursor.execute("SELECT %s FROM %s" % (column, table))
    db.commit()
    return cursor.fetchall()

@app.route("/")
@app.route("/home/")
def home():
    if 'AccountID' in session:
            #admin account
            if session['Type'] == 'Admin':
                return redirect(url_for('admin_display', mode="accounts"))
            else:
                return render_template('home.html', user = session['Name'])
    else:
        return render_template('home.html')

@app.route("/search/", methods= ["POST", "GET"])
def search():
    if request.method == "GET":
        hkey = request.args.getlist("hkey")
        #setup database connection and cursor
        db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
        cursor = db.cursor()
        #sql command
        cursor.execute("""SELECT products.ProductID, categories.category, 
                                    products.ProductName, products.ProductDesc, products.Image, 
                                    products.Quantity, products.Price FROM products
                                    INNER JOIN categories on products.CategoryID = categories.id
                                    WHERE products.ProductName LIKE '%{}%'""".format(hkey[0]))
        db.commit()
        results = cursor.fetchall()
        if len(results) > 0:
            results = list(results)
            for row in range(len(results)):
                results[row-1] = list(results[row-1])
                results[row-1][4] = 'images/' + str(results[row-1][4])

        if 'AccountID' in session:
            #admin account
            if session['Type'] == 'Admin':
                return redirect(url_for('admin_display', mode="accounts"))
            else:
                return render_template('search.html', results = results, hkey = hkey, user = session['Name'])
        else:
            return render_template('search.html', results = results, hkey = hkey)

@app.route("/categories/<string:category>", methods= ["GET"])
def categories(category):
    if request.method == "GET":
        if category == "t_shirts":
            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT products.ProductID, categories.category, 
                                    products.ProductName, products.ProductDesc, products.Image, 
                                    products.Quantity, products.Price FROM products
                                    INNER JOIN categories on products.CategoryID = categories.id
                                    WHERE categories.category = 'T-Shirts'""")
            db.commit()
            results = cursor.fetchall()
            if len(results) > 0:
                results = list(results)
                for row in range(len(results)):
                    results[row-1] = list(results[row-1])
                    results[row-1][4] = 'images/' + str(results[row-1][4])
            if 'AccountID' in session:
                    #admin account
                    if session['Type'] == 'Admin':
                        return redirect(url_for('admin_display', mode="accounts"))
                    else:
                        return render_template('categories.html', user = session['Name'], category=category, results=results)
            else:
                return render_template('categories.html', category=category, results=results)
        if category == "shoes":
            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT products.ProductID, categories.category, 
                                    products.ProductName, products.ProductDesc, products.Image, 
                                    products.Quantity, products.Price FROM products
                                    INNER JOIN categories on products.CategoryID = categories.id
                                    WHERE categories.category = 'Shoes'""")
            db.commit()
            results = cursor.fetchall()
            if len(results) > 0:
                results = list(results)
                for row in range(len(results)):
                    results[row-1] = list(results[row-1])
                    results[row-1][4] = 'images/' + str(results[row-1][4])
            if 'AccountID' in session:
                    #admin account
                    if session['Type'] == 'Admin':
                        return redirect(url_for('admin_display', mode="accounts"))
                    else:
                        return render_template('categories.html', user = session['Name'], category=category, results=results)
            else:
                return render_template('categories.html', category=category, results=results)
        if category == "trackpants":
            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT products.ProductID, categories.category, 
                                    products.ProductName, products.ProductDesc, products.Image, 
                                    products.Quantity, products.Price FROM products
                                    INNER JOIN categories on products.CategoryID = categories.id
                                    WHERE categories.category = 'Trackpants'""")
            db.commit()
            results = cursor.fetchall()
            if len(results) > 0:
                results = list(results)
                for row in range(len(results)):
                    results[row-1] = list(results[row-1])
                    results[row-1][4] = 'images/' + str(results[row-1][4])
            if 'AccountID' in session:
                    #admin account
                    if session['Type'] == 'Admin':
                        return redirect(url_for('admin_display', mode="accounts"))
                    else:
                        return render_template('categories.html', user = session['Name'], category=category, results=results)
            else:
                return render_template('categories.html', category=category, results=results)
        if category == "socks":
            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT products.ProductID, categories.category, 
                                    products.ProductName, products.ProductDesc, products.Image, 
                                    products.Quantity, products.Price FROM products
                                    INNER JOIN categories on products.CategoryID = categories.id
                                    WHERE categories.category = 'Socks'""")
            db.commit()
            results = cursor.fetchall()
            if len(results) > 0:
                results = list(results)
                for row in range(len(results)):
                    results[row-1] = list(results[row-1])
                    results[row-1][4] = 'images/' + str(results[row-1][4])
            if 'AccountID' in session:
                    #admin account
                    if session['Type'] == 'Admin':
                        return redirect(url_for('admin_display', mode="accounts"))
                    else:
                        return render_template('categories.html', user = session['Name'], category=category, results=results)
            else:
                return render_template('categories.html', category=category, results=results)
        if category == "watches":
            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT products.ProductID, categories.category, 
                                    products.ProductName, products.ProductDesc, products.Image, 
                                    products.Quantity, products.Price FROM products
                                    INNER JOIN categories on products.CategoryID = categories.id
                                    WHERE categories.category = 'Watches'""")
            db.commit()
            results = cursor.fetchall()
            if len(results) > 0:
                results = list(results)
                for row in range(len(results)):
                    results[row-1] = list(results[row-1])
                    results[row-1][4] = 'images/' + str(results[row-1][4])
            if 'AccountID' in session:
                    #admin account
                    if session['Type'] == 'Admin':
                        return redirect(url_for('admin_display', mode="accounts"))
                    else:
                        return render_template('categories.html', user = session['Name'], category=category, results=results)
            else:
                return render_template('categories.html', category=category, results=results)

@app.route("/products/<int:item_id>", methods= ["POST", "GET"])
def products(item_id):
    if request.method == "GET":
        #setup database connection and cursor
        db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
        cursor = db.cursor()
        #sql command
        cursor.execute("""SELECT products.ProductID, categories.category, 
                                products.ProductName, products.ProductDesc, products.Image, 
                                products.Quantity, products.Price FROM products
                                INNER JOIN categories on products.CategoryID = categories.id
                                WHERE products.ProductID = %s""" % item_id)
        db.commit()
        results = cursor.fetchall()
        if len(results) > 0:
            results = list(results)
            for row in range(len(results)):
                results[row-1] = list(results[row-1])
                results[row-1][4] = 'images/' + str(results[row-1][4])
        if 'AccountID' in session:
                #admin account
                if session['Type'] == 'Admin':
                    return redirect(url_for('admin_display', mode="accounts"))
                else:
                    return render_template('products.html', user = session['Name'], results=results)
        else:
            return render_template('products.html', results=results)

@app.route("/addcart/<int:acc_id>/<int:item_id>", methods= ["GET"])
def addcart(acc_id, item_id):
    if request.method == "GET":
        #setup database connection and cursor
        db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
        cursor = db.cursor()
        #sql command
        cursor.execute("""INSERT INTO cart (ProductID, AccountID) VALUES (%s, %s)""", (item_id, acc_id))
        db.commit()
        flash('Product added to the cart!', 'success')
        hkey = ['']
        return redirect(url_for('search', hkey = hkey))

@app.route("/cart/<int:acc_id>", methods= ["GET"])
def cart(acc_id):
    if request.method == 'GET':
        #setup database connection and cursor
        db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
        cursor = db.cursor()
        #sql command
        cursor.execute("""SELECT cart.CartID, Account.AccountID, products.ProductID, products.ProductName, products.Price FROM cart
                                INNER JOIN products on cart.ProductID = products.ProductID
                                INNER JOIN Account on cart.AccountID = Account.AccountID
                                WHERE cart.AccountID = %s""" % acc_id)
        db.commit()
        results = cursor.fetchall()

        #calculate total
        total = 0
        for result in results:
            total += result[4]

        if 'AccountID' in session:
                #admin account
                if session['Type'] == 'Admin':
                    return redirect(url_for('admin_display', mode="accounts"))
                else:
                    return render_template('cart.html', user = session['Name'], results=results, total=total)
        else:
            return render_template('cart.html', results=results, total=total)

@app.route("/cart/<int:acc_id>/delete/<int:cart_id>", methods= ["GET"])
def cart_delete(cart_id, acc_id):
    if request.method == 'GET':
        #setup database connection and cursor
        db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
        cursor = db.cursor()
        #sql command
        cursor.execute("DELETE FROM cart WHERE CartID = %d" % cart_id)
        db.commit()

        flash(f"Product deleted from the cart!", "danger")
        return redirect(url_for('cart', acc_id = acc_id))

@app.route("/addorders/<int:acc_id>", methods= ["GET"])
def addorders(acc_id):
    if request.method == 'GET':
        #setup database connection and cursor
        db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
        cursor = db.cursor()
        #sql command
        cursor.execute("""SELECT cart.CartID, Account.AccountID, products.ProductID FROM cart
                                INNER JOIN products on cart.ProductID = products.ProductID
                                INNER JOIN Account on cart.AccountID = Account.AccountID
                                WHERE cart.AccountID = %s""" % acc_id)
        db.commit()
        results = cursor.fetchall()

        for result in results:
            cursor.execute("INSERT INTO OrderDesc (ProductID, AccountID, OrderDate) VALUES (%s, %s, NOW())", (result[2], result[1]))
            db.commit()
            cursor.execute("DELETE FROM cart WHERE CartID = %s" % result[0])
            db.commit()

        flash(f"Order created!", "success")
        return redirect(url_for('orders', acc_id = acc_id))

@app.route("/orders/<int:acc_id>", methods= ["GET"])
def orders(acc_id):
    if request.method == 'GET':
        #setup database connection and cursor
        db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
        cursor = db.cursor()
        #sql command
        cursor.execute("""SELECT OrderDesc.OrderID, Account.AccountID, products.ProductName, products.Price, OrderDesc.OrderDate FROM OrderDesc
                                INNER JOIN products on OrderDesc.ProductID = products.ProductID
                                INNER JOIN Account on OrderDesc.AccountID = Account.AccountID
                                WHERE OrderDesc.AccountID = %s""" % acc_id)
        db.commit()
        results = cursor.fetchall()

        if 'AccountID' in session:
                #admin account
                if session['Type'] == 'Admin':
                    return redirect(url_for('admin_display', mode="accounts"))
                else:
                    return render_template('orders.html', user = session['Name'], results=results)
        else:
            return render_template('orders.html', results=results)

@app.route("/about/")
def about():
    if 'AccountID' in session:
            #admin account
            if session['Type'] == 'Admin':
                return redirect(url_for('admin_display', mode="accounts"))
            else:
                return render_template('about.html', user = session['Name'])
    else:
        return render_template('about.html')

@app.route("/contact/")
def contact():
    if 'AccountID' in session:
            #admin account
            if session['Type'] == 'Admin':
                return redirect(url_for('admin_display', mode="accounts"))
            else:
                return render_template('contact.html', user = session['Name'])
    else:
        return render_template('contact.html')

@app.route("/login/", methods= ["POST", "GET"])
def login():
    form = LoginPage()
    if request.method == 'POST' and form.validate_on_submit():
        # login successfully
        try:
            name = request.form['username']
            pw = request.form['password']
            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("SELECT AccountID, Type, Name, Password FROM Account WHERE Name = %s", (name))
            db.commit()

            results = cursor.fetchall()
            for row in results:
                acc_id = row[0]
                acc_type = row[1]
                acc_name = row[2]
                acc_pw = row[3]
                #session
                session['Name'] = acc_name
                session['AccountID'] = acc_id
                session['Type'] = acc_type
                session['Password'] = acc_pw

            if session["Password"] == pw:
                #admin account
                if session['Type'] == 'Admin':
                    flash(f'Welcome, %s!'%session['Name'], 'success')
                    return redirect(url_for('admin_display', mode="accounts"))
                else:
                    flash(f'Welcome, %s!'%session['Name'], 'success')
                    return redirect(url_for('home'))
            else:
                flash('Failed to Login, please check the username and/or password.', 'danger')
                return redirect(url_for('login'))
        except:
            flash('Failed to Login, please check your username and/or password.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', title = 'Login', form = form)

@app.route("/logout/")
def logout():
    #logout
    session.pop('Name', None)
    session.pop('AccountID', None)
    session.pop('Type', None)
    session.pop('Password', None)
    flash('You have successfully logged out!', 'danger')
    return render_template('home.html')

@app.route("/sign_up/", methods= ["POST", "GET"])
def register():
    form = SignUp()
    if request.method == 'POST' and form.validate_on_submit():
        name = request.form['username']
        email = request.form['email']
        pw = request.form['password']
        #setup database connection and cursor
        db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
        cursor = db.cursor()
        #sql command
        cursor.execute("INSERT INTO Account (Type, Name, Email, Password) VALUES ('User', %s, %s, %s)", (name, email, pw))
        db.commit()

        flash(f'Account created for '+name+'.', 'success')
        return redirect(url_for('home'))
    return render_template('sign_up.html', title='Sign Up', form = form)

@app.route('/admin/display/<string:mode>', methods= ["POST", "GET"])
def admin_display(mode):
    if request.method == "GET":
        if mode == "accounts":
            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("SELECT * FROM Account")
            db.commit()
            results = cursor.fetchall()
            cursor.execute("DESC Account")
            db.commit()
            field_names = cursor.fetchall()

            return render_template('admin_display.html', user = session['Name'], mode=mode, results=results, field_names=field_names)

        if mode == "products":
            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT products.ProductID, categories.category, 
                                    products.ProductName, products.ProductDesc, products.Image, 
                                    products.Quantity, products.Price FROM products
                                    INNER JOIN categories on products.CategoryID = categories.id""")
            db.commit()
            results = cursor.fetchall()
            #decrease the number of text shown in display
            if len(results) > 0:
                results = list(results)
                for row in range(len(results)):
                    results[row-1] = list(results[row-1])
                    if len(results[row-1][3]) > 25:
                        results[row-1][3] = str(results[row-1][3][:25]) + "..."
                    if len(str(results[row-1][4])) > 10:
                        results[row-1][4] = str(results[row-1][4][:25]) + "..."
                    results[row-1][4] = 'images/' + str(results[row-1][4])
            #obtain column names from other tables
            cursor.execute("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA` = 'ink' AND `TABLE_NAME` IN ('Category') AND `COLUMN_NAME` LIKE '%Name';")
            db.commit()
            foreign_names = cursor.fetchall()
            cursor.execute("DESC products")
            db.commit()
            field_names = cursor.fetchall()

            return render_template('admin_display.html', user = session['Name'], mode=mode, results=results, field_names=field_names, foreign_names=foreign_names)

        if mode == "orders":            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT OrderDesc.OrderID, products.ProductID, products.ProductName, 
                                    products.Price, Account.AccountID, Account.Name, OrderDesc.OrderDate FROM OrderDesc
                                    INNER JOIN Account on OrderDesc.AccountID = Account.AccountID
                                    INNER JOIN products on OrderDesc.ProductID = products.ProductID""")
            db.commit()
            results = cursor.fetchall()
            #obtain column names from other tables
            cursor.execute("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA` = 'ink' AND `TABLE_NAME` IN ('Account', 'products') AND `COLUMN_NAME` LIKE '%Name';")
            db.commit()
            foreign_names = cursor.fetchall()
            cursor.execute("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA` = 'ink' AND `TABLE_NAME` IN ('products') AND `COLUMN_NAME` LIKE '%Price';")
            db.commit()
            price_name = cursor.fetchall()
            cursor.execute("DESC OrderDesc")
            db.commit()
            field_names = cursor.fetchall()

            return render_template('admin_display.html', user = session['Name'], mode=mode, results=results, field_names=field_names, foreign_names=foreign_names, price_name=price_name)

@app.route('/admin/display/<string:mode>/delete/<int:item_id>', methods= ["POST", "GET"])
def admin_delete(mode, item_id):
    if request.method == 'GET':
        if mode == "accounts":
            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("DELETE FROM Account WHERE AccountID = %d" % item_id)
            db.commit()

            flash(f"Account deleted", "danger")
            return redirect(url_for('admin_display', mode="accounts"))

        if mode == "products":
            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("DELETE FROM products WHERE ProductID = %d" % item_id)
            db.commit()

            flash(f"Product deleted", "danger")
            return redirect(url_for('admin_display', mode="products"))

        if mode == "orders":
            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("DELETE FROM OrderDesc WHERE OrderID = %d" % item_id)
            db.commit()

            flash(f"Order cancelled", "danger")
            return redirect(url_for('admin_display', mode="orders"))

@app.route('/admin/display/<string:mode>/create', methods= ["POST", "GET"])
def admin_create(mode):
    if mode == "accounts":
        form = Admin_Account()
        formfield = [getattr(form, 'acctype'), getattr(form, 'username'),
                    getattr(form, 'email'), getattr(form, 'password'),
                    getattr(form, 'confirm_password')]

        if request.method == 'POST':
            acc_type = request.form['acctype']
            name = request.form['username']
            email = request.form['email']
            pw = request.form['password']
            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("INSERT INTO Account (Type, Name, Email, Password) VALUES (%s, %s, %s, %s)", (acc_type, name, email, pw))
            db.commit()

            flash(f'Account created for '+name+'.', 'success')
            return redirect(url_for('admin_display', mode="accounts"))

    elif mode == "products":
        form = Admin_Product()
        form.categoryid.choices = []
        #add dynamic choices dependent from another table
        for row in fetch_items('categories', '*'):
            form.categoryid.choices += [(str(row[0]), row[1])]

        formfield = [getattr(form, 'categoryid'),
                    getattr(form, 'productname'), getattr(form, 'productdesc'), 
                    getattr(form, 'picture'), getattr(form, 'quantity'), 
                    getattr(form, 'price')]

        if request.method == 'POST':
            category_id = request.form['categoryid']
            product_name = request.form['productname']
            product_desc = request.form['productdesc']
            image = request.form['picture']
            quantity = request.form['quantity']
            price = request.form['price']

            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("INSERT INTO products (CategoryID, ProductName, ProductDesc, Image, Quantity, Price) VALUES (%s, %s, %s, %s, %s, %s)", (category_id, product_name, product_desc, image, quantity, price))
            db.commit()

            flash(f'Product created for '+product_name+'.', 'success')
            return redirect(url_for('admin_display', mode="products"))


    return render_template('admin_create.html', form = form, mode = mode, formfield = formfield)

@app.route('/admin/display/<string:mode>/edit/<int:item_id>', methods= ["POST", "GET"])
def admin_edit(mode, item_id):
    if mode == "accounts":
        form = Admin_EditPage()
        if request.method == 'GET':
            #formfield for getting text input boxes
            formfield = [getattr(form, 'acctype'), getattr(form, 'username'),
                        getattr(form, 'email'), getattr(form, 'password'), 
                        getattr(form, 'confirm_password')]
            #fieldvalues for selected file's original values
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("SELECT Type, Name, Email, Password FROM Account WHERE AccountID = %d" % item_id)
            db.commit()

            results = cursor.fetchall()
            return render_template('admin_edit.html', form = form, mode = mode, formfield = formfield, results = results, item_id = item_id)
        if request.method == 'POST':
            acc_type = request.form['acctype']
            name = request.form['username']
            email = request.form['email']
            pw = request.form['password']
            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("UPDATE Account SET Type = %s, Name = %s, Email = %s, Password = %s WHERE AccountID = %s", (acc_type, name, email, pw, item_id))
            db.commit()

            flash(f'Account edited for '+name+'.', 'success')
            return redirect(url_for('admin_display', mode="accounts"))

    elif mode == "products":
        form = Admin_Product()
        form.categoryid.choices = []
        #add dynamic choices dependent from another table
        for row in fetch_items('categories', '*'):
            form.categoryid.choices += [(str(row[0]), row[1])]

        if request.method == 'GET':
            #formfield for getting text input boxes
            formfield = [getattr(form, 'categoryid'),
                        getattr(form, 'productname'), getattr(form, 'productdesc'), 
                        getattr(form, 'picture'), getattr(form, 'quantity'), 
                        getattr(form, 'price')]
            #fieldvalues for selected file's original values
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT categories.category, 
                                    products.ProductName, products.ProductDesc, products.Image, 
                                    products.Quantity, products.Price FROM products
                                    INNER JOIN categories on products.CategoryID = categories.id
                                    WHERE products.ProductID = %s""" % item_id)
            db.commit()

            results = cursor.fetchall()
            return render_template('admin_edit.html', form = form, mode = mode, formfield = formfield, results = results, item_id = item_id)
        if request.method == 'POST':
            category_id = request.form['categoryid']
            product_name = request.form['productname']
            product_desc = request.form['productdesc']
            image = request.form['picture']
            quantity = request.form['quantity']
            price = request.form['price']
            #setup database connection and cursor
            db = pymysql.connect(host='localhost',user='kalvin',password='93148325',database='rainbow')
            cursor = db.cursor()
            #sql command
            cursor.execute("""UPDATE products SET CategoryID = %s, ProductName = %s, 
                                    ProductDesc = %s, Image = %s, Quantity = %s, Price = %s 
                                    WHERE ProductID = %s""", (category_id, product_name, product_desc, image, quantity, price, item_id))
            db.commit()

            flash(f'Product edited for '+product_name+'.', 'success')
            return redirect(url_for('admin_display', mode="products"))

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="8000")