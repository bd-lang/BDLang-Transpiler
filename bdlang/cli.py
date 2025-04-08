# CLI entry point
import argparse
from .transpiler import transpile

def main():
    parser = argparse.ArgumentParser(description="BDLang Bangla-to-Python Transpiler")
    parser.add_argument("filepath", help="Path to .bdl file")
    args = parser.parse_args()

    with open(args.filepath, encoding='utf-8') as f:
        bangla_code = f.read()
    output = transpile(bangla_code)
    print("🔁 Transpiled Python Code:")
    print(output)

if __name__ == "__main__":
    main()
