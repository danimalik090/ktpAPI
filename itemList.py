from flask import Flask, render_template, json, request, redirect
import requests
import simplejson

itemList = Flask(__name__)
url = 'https://gist.githubusercontent.com/chamathpali/7cccd0ff8a0338645559e5ed468231fa/raw/3a467ff8807a090cbdbe5e4583b8d07b925a7979/items.json'
data = requests.get(url)
jsondata = data.content
items = simplejson.loads(jsondata)



@itemList.route("/refresh", methods = ['GET'])
def refresh():
    url = 'https://gist.githubusercontent.com/chamathpali/7cccd0ff8a0338645559e5ed468231fa/raw/3a467ff8807a090cbdbe5e4583b8d07b925a7979/items.json'
    data = requests.get(url)
    jsondata = data.content
    items = simplejson.loads(jsondata)
    return render_template("index.html", items=items)

@itemList.route("/")
def main():
    #items = simplejson.loads(jsondata)
    return render_template("index.html", items = items)

@itemList.route("/additem", methods = ['GET','POST'])
def additem():
    if request.method == 'GET':
        return render_template("additem.html", item = {})
    if request.method == 'POST':
        id = int(request.form["id"])
        name = request.form["name"]
        price = request.form["price"]
        quantity = request.form["quantity"]
        items.append({"id": id, "name": name, "price": price, "quantity": quantity})
        return redirect('/')
@itemList.route('/updateitem/<int:id>',methods = ['GET','POST'])
def updateitem(id):
    if request.method == 'GET':
        item = [item for item in items if item['id'] == id][0]
        return render_template("additem.html", item = item)
    if request.method == 'POST':
        for item in items:
            if(item['id'] == id):
                item['name'] = request.form["name"]
                item['price'] = request.form["price"]
                item['quantity'] = request.form["quantity"]
                break
        return redirect('/')
@itemList.route('/deleteitem/<int:id>')
def deleteitem(id):
    item = [item for item in items if item['id'] == id]
    items.remove(item[0])
    return redirect('/')

if(__name__ == "__main__"):
    itemList.run()