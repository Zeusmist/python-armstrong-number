from flask import Flask, render_template, request, flash, redirect
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)


def find_armstrong(three_digit_number):
    if three_digit_number >= 100 and three_digit_number <= 999:
        # convert the number to string, then iterate over each number to perform the algorithm
        cubeSum = 0
        stringified = str(three_digit_number)
        for x in stringified:
            cubeSum += int(x) * int(x) * int(x)
        if cubeSum == three_digit_number:
            return (f"{three_digit_number} is an Armstrong number", "successful")
            # print("Armstrong number")
        else:
            return (f"{three_digit_number} is not an Armstrong number", "error")
            # print("Not armstrong number")
    else:
        return (f"{three_digit_number} is not a three digit number", "error")
        # print("Not a three digit number")
        # return


class NumberForm(FlaskForm):
    class Meta:
        csrf = False
    number = IntegerField(label="3 digit number", validators=[
                          InputRequired(), NumberRange(min=100, max=999)])


@app.route("/", methods=["GET"])
def index():
    form = NumberForm()
    return render_template("index.html", form=form)


@app.route("/reg", methods=["GET", "POST"])
def check():
    form = NumberForm()
    if request.method == "POST":
        if form.validate_on_submit():
            number = form.number.data
            result, status = find_armstrong(number)

            flash(result, status)
            return redirect("/")
        else:
            flash("Invalid input provided")
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.secret_key = "secret"
    app.run(debug=True)
