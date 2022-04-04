from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/depression")
def depression():
    return render_template("depression.html")




@app.route("/obesity", methods=["GET", "POST"])
def obesity():
    if request.method == "POST":

        height = int(request.form.get("height"))
        weight = int(request.form.get("weight"))

        BMI = (weight / (height/100)**2)


        if BMI <= 18.4:
            return render_template("answerbmi.html", result="You are underweight.")
        elif BMI <= 24.9:
            return render_template("answerbmi.html", result="You have healthy weight")
        elif BMI <= 29.9:
            return render_template("answerbmi.html", result="You are overweight ")
        elif BMI <= 34.9:
            return render_template("answerbmi.html", result="You are severely overweight")
        elif BMI <= 39.9:
            return render_template("answerbmi.html", result="You are obese")
        else:
            return render_template("answerbmi.html", result="You are severely obese ")


        return redirect("/")
    else:
        return render_template("obesity.html")



@app.route("/hypertension")
def hypertension():
    return render_template("hypertension.html")



@app.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")


@app.route("/atherosclerosis")
def atherosclerosis():
    return render_template("atherosclerosis.html")


@app.route("/diab1")
def diab1():
    return render_template("diab1.html")


@app.route("/diabe2")
def diabe2():
    return render_template("diabe2.html")




