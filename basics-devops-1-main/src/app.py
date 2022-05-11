from flask import Flask, request
from src.functional import process, number_prep # noqa

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['GET'])
def calculate() -> dict:
    f_numb = request.args.get('first_numb')
    s_numb = request.args.get('second_numb')
    operator = request.args.get('operator')
    replacee = {'minus': '-', 'plus': '+', 'del': '/', 'mult': '*'}
    operator = replacee.get(operator)  # type: ignore
    rezult = process(
        number_prep(f_numb), number_prep(s_numb), operator)  # type: ignore
    return {"rezult": rezult}


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
