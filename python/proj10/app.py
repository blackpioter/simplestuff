from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
import pandas as pd
from geopy.geocoders import ArcGIS
import datetime
import os


app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['post'])
def success():
    global filename
    if request.method=='POST':
        file=request.files["file"]
        data = pd.read_csv(file)

        if any([item in data.columns for item in ['Address','address']]):
            nom = ArcGIS()
            # data["Full address"] = data["Address"] + data["Locality"]
            if set(['Address']).issubset(data.columns):
                data["Coordinates"] = data["Address"].apply(nom.geocode)
            else:
                data["Coordinates"] = data["address"].apply(nom.geocode)
            data["Latitude"] = data["Coordinates"].apply( lambda x: x.latitude if x != None else None)
            data["Longitude"] = data["Coordinates"].apply( lambda x: x.longitude if x != None else None)
            data=data.drop("Coordinates",1)

            uploads_dir="uploads/"
            if not os.path.exists(uploads_dir):
                os.makedirs(uploads_dir)

            filename=datetime.datetime.now().strftime(uploads_dir + "%Y-%m-%d-%H-%M-%S-%f"+".csv")
            data.to_csv(filename)
            return render_template("index.html", text=data.to_html(), btn='download.html')
        else:
            return render_template("index.html", text="Your CSV file does not have address column !")

@app.route("/download")
def download():
    return send_file(filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == "__main__":
    app.debug = True
    app.run()
