from flask import Flask, render_template

app = Flask(__name__)


@app.route('/plot/')
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure
    # data.DataReader?
    from bokeh.embed import components
    from bokeh.resources import CDN

    start = datetime.datetime(2015, 11, 1)
    end = datetime.datetime(2016, 3, 10)
    df = data.DataReader("GOOG", "yahoo", start, end)

    hours_12 = 43200000  # 12 hours to msec

    def inc_dec(c, o):
        if c > o:
            value = "Increase"
        elif c < o:
            value = "Decrease"
        else:
            value = "Equal"
        return value

    df["Status"] = [inc_dec(c, o) for c, o in zip(df["Close"], df["Open"])]

    df["Middle"] = (df["Open"]+df["Close"])/2

    df["Height"] = abs(df["Open"]-df["Close"])

    p = figure(x_axis_type="datetime", width=1000,
               height=300, sizing_mode="scale_width")
    p.title.text = "Candlestick Chart"
    p.grid.grid_line_alpha = 0.3

    p.segment(df.index, df.High, df.index, df.Low, color="black")
    p.rect(x=df.index[df["Status"] == "Increase"],
           y=df[df["Status"] == "Increase"]["Middle"],
           width=hours_12,
           height=df[df["Status"] == "Increase"]["Height"],
           fill_color='#CCFFFF',
           line_color="black")
    p.rect(x=df.index[df["Status"] == "Decrease"],
           y=df[df["Status"] == "Decrease"]["Middle"],
           width=hours_12,
           height=df[df["Status"] == "Decrease"]["Height"],
           fill_color='#FF3333',
           line_color="black")

    script, div = components(p)
    cdn_js = CDN.js_files

    return render_template("plot.html",
                           script=script,
                           div=div,
                           cdn_js=cdn_js[0])


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
