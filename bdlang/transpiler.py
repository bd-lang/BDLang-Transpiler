# Transpiler: Converts Bangla code to Python code
def transpile(bangla_code):
    from .parser import parse
    parsed = parse(bangla_code)
    return parsed  # TODO: convert parse tree to Python code
