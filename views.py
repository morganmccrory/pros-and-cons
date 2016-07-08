from flask import render_template, redirect, request, url_for
from pros_and_cons import app
from pros_and_cons.models import List, Pro, Con

@app.route("/")
def home():
  return render_template("lists/index.html", lists=List.objects.all())

@app.route("/lists/<slug>")
def show_list(slug):
  list = List.objects.get(slug=slug)
  return render_template("lists/show.html", list=list)

@app.route("/lists/create", methods=["GET", "POST"])
def create_list():
  if request.method == "GET":
    return render_template("lists/new.html")
  else:
    name = request.form["name"]
    slug = request.form["slug"]

    list = List(name=name, slug=slug)
    list.save()

    return redirect("/")

@app.route("/lists/<slug>/edit", methods=["GET", "POST"])
def update_list(slug):
  if request.method == "GET":
    list = List.objects.get(slug=slug)
    return render_template("lists/edit.html", list=list)
  else:
    name = request.form["name"]
    slug = request.form["slug"]

    list = List.objects.get(slug=slug)
    list.update(name=name, slug=slug)
    list.save()

    return redirect("/")

@app.route("/lists/<slug>/delete", methods=["POST"])
def delete_list(slug):
  list = List.objects.get(slug=slug)
  list.delete()
  return redirect("/")

@app.route("/lists/<slug>/pros/create", methods=["GET", "POST"])
def create_pro(slug):
  if request.method == "GET":
    list = List.objects.get(slug=slug)
    return render_template("/lists/pros/new.html", list=list)
  else:
    slug = request.form["slug"]
    body = request.form["body"]
    pro = Pro(body=body)

    list = List.objects.get(slug=slug)
    list.pros.append(pro)
    list.save()

    return redirect("/lists/" + slug)

@app.route("/lists/<slug>/cons/create", methods=["GET", "POST"])
def create_con(slug):
  if request.method == "GET":
    list = List.objects.get(slug=slug)
    return render_template("/lists/cons/new.html", list=list)
  else:
    slug = request.form["slug"]
    body = request.form["body"]
    con = Con(body=body)

    list = List.objects.get(slug=slug)
    list.cons.append(con)
    list.save()

    return redirect("/lists/" + slug)