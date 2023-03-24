import os
import base64
import math

class Colors: 
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    WHITE = "\033[37m"

Types = {
    'bintohex': {
        'run': lambda bin_: hex(int(bin_, 2)),
        'description': 'Converts a binary number to hexadecimal'
    },
    'hextobin16': {
        'run': lambda hex_: bin(int(hex_, 16)),
        'description': 'Converts a hexadecimal number to a binary number with 16 bits'
    },
    'hextobin': {
        'run': lambda hex_: bin(int(str(hex_), 16))[:2],
        'description': 'Converts a hexadecimal number to a binary number'
    },
    'inttofloat': {
        'run': lambda num: int(int(num)/1.0) or float(int(num)),
        'description': 'Converts an integer to a float'
    },
    'stringtohex': {
        'run': lambda string: str(string).encode('utf-8').hex(),
        'description': 'Converts a string to a hexadecimal number'
    },
    'hextostring': {
        'run': lambda hex_: bytearray.fromhex(hex_[2:]).decode('utf-8'),
        'description': 'Converts a hexadecimal number to a string'
    },
    'hextoint': {
        'run': lambda hex_: int(str(hex_), 16),
        'description': 'Converts a hexadecimal number to an integer'
    },
    'floattointr': {
        'run': lambda flt: round(float(flt)),
        'description': 'Converts a float to an integer using rounding'
    },
    'floattoint': {
        'run': lambda flt: int(float(flt)),
        'description': 'Converts a float to an integer by truncating decimal points'
    },
    'stringtobin': {
        'run': lambda string: ''.join(format(ord(c), '08b') for c in string),
        'description': 'Converts a string to an binary number'
    },
    'bintoint': {
        'run': lambda bin_: int(bin_, 2),
        'description': 'Converts a binary number to an integer'
    },
    'bintostring': {
        'run': lambda bin_: "".join([chr(int(bin_[i:i+8], 2)) for i in range(0, len(bin_), 8)]),
        'description': 'Converts a binary number to an string'
    },
    'inttobin': {
        'run': lambda num: bin(int(num))[2:],
        'description': 'Converts an integer to a binary number'
    },
    'inttohex': {
        'run': lambda num: hex(int(num)),
        'description': 'Converts an integer to a hexadecimal number'
    },
    'stringtob64': {
        'run': lambda string: base64.b64encode(string.encode("utf-8")).decode("utf-8"),
        'description': 'Converts a string to base64 encode'
    },
    'b64tostring': {
        'run': lambda b64: base64.b64decode(b64).decode("utf-8"),
        'description': 'Converts a base64 to a string'
    },
    'stringtoupper': {
        'run': lambda string: str(string).upper(),
        'description': 'String to upper string'
    },
    'stringtolower': {
        'run': lambda string: str(string).lower(),
        'description': 'String to lower string'
    },
    'stringtoeval': {
        'run': lambda string: eval(str(string)),
        'description': 'Convert string to value in a eval (math.<funcs> included)'
    }
}

class Main:
    def __init__(self) -> None:
        
        while True:
            self.clear()
            print("""
                  {}
              ConverterType v1.0 by SebDev
        ----------------------------------------
                Simple change the type
                    of other type
              """.format(Colors.WHITE))
            command = input("> ")
            
            if command == "help":
                keys = Types.keys()
                for key in keys:
                    print("{}{} {}- {}{}".format(Colors.YELLOW, key, Colors.RED, Colors.GREEN, Types.get(key).get("description")))
                    
                input("")
            elif command == "exit":
                exit(0)
            else:
                if Types.get(command) is not None:
                    try:
                        arg = input("> ")
                        print("Converting ({})...".format(arg))
                        print("""
        {}{} --> {} 
        {}   {}
                              """.format(Colors.GREEN, arg, command, Colors.YELLOW, Types[command]["run"](arg)))
                        input("")
                    except:
                        print("{}Error when converting! ({})".format(Colors.RED, command))
                        input("")
                else:
                    print("{}Command not found! ({})".format(Colors.RED, command))
                    input("")
    
    def clear(self):      
        if 'nt' in os.name: 
            os.system("cls")
        else:
            os.system("clear") 
    
if __name__ == "__main__":
    main = Main()
