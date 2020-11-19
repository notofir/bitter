from flask import Flask, render_template, request, jsonify, make_response

app = Flask(__name__)
BITS_PER_LINE = 30
LINES_PER_LOAD = 100


def load_next(file, seek):
    file.seek(seek)
    lines = []
    for _ in range(LINES_PER_LOAD):
        line = file.read(BITS_PER_LINE)
        if line == "":
            break

        lines.append(line)

    return dict(
        has_more=bool(file.read(1)),
        lines=lines
    )


def load_prev(file, seek):
    offset = max((seek - BITS_PER_LINE * LINES_PER_LOAD, 0))
    file.seek(offset)
    data = file.read(min((seek, BITS_PER_LINE * LINES_PER_LOAD)))
    lines = []
    i = seek
    for i in range(len(data) - BITS_PER_LINE, 0, -BITS_PER_LINE):
        lines.append(data[i: i + BITS_PER_LINE])

    lines.append(data[0: i])
    return dict(
        has_more=bool(offset),
        lines=lines
    )


@app.route("/")
def index():
    return render_template("index.html", lines_per_load=LINES_PER_LOAD, bits_per_line=BITS_PER_LINE)


@app.route("/load")
def load():
    if not request.args:
        return

    seek = int(request.args.get("seek"))
    direction = request.args.get("direction")
    options = {
        "prev": load_prev,
        "next": load_next
    }
    with open("binary.bin", "r") as file:
        return make_response(jsonify(options[direction](file, seek)), 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
