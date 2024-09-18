from .. import app


@app.get("/calculate/{exp}")
def calculate(exp: str):
    try:
        if "+" in exp:
            num1, num2 = exp.split("+")
            return {"result": int(num1) + int(num2)}
        elif "-" in exp:
            num1, num2 = exp.split("-")
            return {"result": int(num1) - int(num2)}
        else:
            return {"error": "Invalid operation"}
    except ValueError:
        return {"error": "Invalid input"}