import os
import base64
import re
import hashlib
import math
import requests
import json

libs = [math.__name__, 
        base64.__name__, 
        os.__name__, 
        requests.__name__, 
        re.__name__,
        json.__name__,
        hashlib.__name__]

class Colors: 
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    WHITE = "\033[37m"

square = "²"

Ms_Converters = {
    'mtom2': {
        'run': lambda a: f"{a[0]*a[1]} m{square}",
        'fields': ["height", "width"],
        'description': 'Meters to Square Meters (x * y)'
    },
    'mmtom': {
        'run': lambda a: f"{a[0]/1000} m",
        'fields': ["(mm)"],
        'description': 'Millimeters to Metters (x/1000)'
    },
    'mtomm': {
        'run': lambda a: f"{a[0]*1000} mm",
        'fields': ["(m)"],
        'description': 'Meters to Millimetters (x*1000)'
    },
    'mtokm': {
        'run': lambda a: f"{a[0]/1000} km",
        'fields': ["(m)"],
        'description': 'Meters to Kilometres (x/1000)'
    },
    'kmtom': {
        'run': lambda a: f"{a[0]*1000} m",
        'fields': ["(km)"],
        'description': 'Kilometres to Meters (x*1000)'
    },
    'ltoml': {
        'run': lambda a: f"{a[0] * 1000} mL",
        'fields': ["(L)"],
        'description': 'Liters to Milliliters (x * 1000)'
    },
    'mltol': {
        'run': lambda a: f"{a[0] / 1000} L",
        'fields': ["(mL)"],
        'description': 'Milliliters to Liters (x / 1000)'
    },
    'gtomg': {
        'run': lambda a: f"{a[0] * 1000} mg",
        'fields': ["(g)"],
        'description': 'Grams to Milligrams (x * 1000)'
    },
    'mgtog': {
        'run': lambda a: f"{a[0] / 1000} g",
        'fields': ["(mg)"],
        'description': 'Milligrams to Grams (x / 1000)'
    }
}

Plugins = []
Custom = {}

# api version = 1
Types = {
    'apiversion': 1,
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
    # base64
    'stringtob64': {
        'run': lambda string: base64.b64encode(string.encode("utf-8")).decode("utf-8"),
        'description': 'Converts a string to base64 encode'
    },
    'b64tostring': {
        'run': lambda b64: base64.b64decode(b64).decode("utf-8"),
        'description': 'Converts a base64 to a string'
    },
    # base16
    'stringtob16': {
        'run': lambda string: base64.b16encode(string.encode("utf-8")).decode("utf-8"),
        'description': 'Converts a string to base16 encode'
    },
    'b16tostring': {
        'run': lambda b64: base64.b16decode(b64).decode("utf-8"),
        'description': 'Converts a base16 to a string'
    },
    # base32
    'stringtob32': {
        'run': lambda string: base64.b32encode(string.encode("utf-8")).decode("utf-8"),
        'description': 'Converts a string to base32 encode'
    },
    'b32tostring': {
        'run': lambda b32: base64.b32decode(b32).decode("utf-8"),
        'description': 'Converts a base32 to a string'
    },
    # base85
    'stringtob85': {
        'run': lambda string: base64.b85encode(string.encode("utf-8")).decode("utf-8"),
        'description': 'Converts a string to base85 encode'
    },
    'b85tostring': {
        'run': lambda b85: base64.b85decode(b85).decode("utf-8"),
        'description': 'Converts a base85 to a string'
    },
    # base ascii85
    'stringtoa85': {
        'run': lambda string: base64.a85encode(string.encode("utf-8")).decode("utf-8"),
        'description': 'Converts a string to base64 like ascii85 encode'
    },
    'a85tostring': {
        'run': lambda a85: base64.a85decode(a85).decode("utf-8"),
        'description': 'Converts a base64 like ascii85 to a string'
    },
    # end base64 lines
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
    },
    'hextorgb': {
        'run': lambda hex_: tuple(int(hex_.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)),
        'description': 'Convert hex color code to RGB tuple'
    },
    'rgbtohex': {
        'run': lambda rgb: f"#{''.join(map(lambda x: hex(int(x))[2:].zfill(2), str(rgb).strip('()').replace(' ', '').split(',')))}" if re.match(r'^\(\s*\d{1,3}\s*,\s*\d{1,3}\s*,\s*\d{1,3}\s*\)$', rgb) else 1/0,
        'description': 'Convert RGB tuple to hex color code'
    },
    # hashlib utils
    'stringtoh256': {
        'run': lambda string: hashlib.sha256(string.encode('utf-8')).hexdigest(),
        'description': 'Encrypt an string to a hex SHA-256(unhashable)'
    },
    'stringtoh512': {
        'run': lambda string: hashlib.sha512(string.encode('utf-8')).hexdigest(),
        'description': 'Encrypt an string to a hex SHA-512(unhashable)'
    },
    'stringtoh1': {
        'run': lambda string: hashlib.sha1(string.encode('utf-8')).hexdigest(),
        'description': 'Encrypt an string to a hex SHA-1(unhashable)'
    },
    'stringtoh224': {
        'run': lambda string: hashlib.sha224(string.encode('utf-8')).hexdigest(),
        'description': 'Encrypt an string to a hex SHA-224(unhashable)'
    },
    'stringtoh384': {
        'run': lambda string: hashlib.sha384(string.encode('utf-8')).hexdigest(),
        'description': 'Encrypt an string to a hex SHA-384(unhashable)'
    }
}

class Plugin:
    def __init__(self, file) -> None:
        self.file = file

class Main:
    def __init__(self) -> None:
        
        # RUN PLUGINS
        
        for i in os.walk("plugins"):
            plugin = Plugin(i[2][0])
            self.loadPlugin(plugin=plugin)
            
        for i in Plugins:
            Custom[i["plugin"]["name"]] = {
                "description": i["plugin"]["description"],
                "run": [k for k in i["data"]]
            }
        
        while True:
            self.clear()
            print("""
                  {}
             ConverterType v1.4 by SebDev
        --------------------------------------
                Simple change the type
                    of other type
                    
                      Commands:
                  help | exit | api
        --------------------------------------
              """.format(Colors.WHITE))
            command = input("> ")
            
            if command == "help":
                keys = Types.keys()
                for key in keys:
                    if key == "apiversion":
                        continue
                    else:
                        print("{}{} {}- {}{}".format(Colors.YELLOW, key, Colors.RED, Colors.GREEN, Types.get(key).get("description")))
                print(Colors.WHITE+"========= Measures =========")
                keys = Ms_Converters.keys()
                for key in keys:
                    print("{}{} {}- {}{}".format(Colors.YELLOW, key, Colors.RED, Colors.GREEN, Ms_Converters.get(key).get("description")))
                print(Colors.WHITE+"=========  CUSTOMS  =========")
                keys = Custom.keys()
                for key in keys:
                    print("{}{} {}- {}{}".format(Colors.YELLOW, key, Colors.RED, Colors.GREEN, Custom.get(key).get("description")))
                input("")
            elif command == "exit":
                exit(0)
            elif command == "api":
                print(f"""
                      {Colors.GREEN}from {Colors.YELLOW}converter {Colors.GREEN}import {Colors.YELLOW}ConverterAPI
                      
                      {Colors.WHITE}api = {Colors.YELLOW}ConverterAPI(version=1)
                      
                      {Colors.WHITE}# Convert 'Hello, World!' to Sha256(undecryptable) hex digest
                      {Colors.RED}print({Colors.YELLOW}output_type='stringtoh256', input_value='Hello, World!'{Colors.RED})
                      """)
                
                input("")
            else:
                if len(command.split(" ")) == 2 and command.split(" ")[0] == "help":
                    
                    arg = command.split(" ")[1]
                    
                    if Types.get(arg) is not None:
                        print("{}{}:{} {}".format(Colors.GREEN, arg, Colors.YELLOW, Types.get(arg).get("description")))
                    elif Ms_Converters.get(arg) is not None:
                        print("{}{}:{} {}".format(Colors.GREEN, arg, Colors.YELLOW, Ms_Converters.get(arg).get("description")))
                    elif Custom.get(arg) is not None:
                        print("{}{}:{} {}".format(Colors.GREEN, arg, Colors.YELLOW, Custom.get(arg).get("description")))
                        print(Colors.WHITE+"=============== FUNCTIONS ===============")
                        for i in Custom.get(arg)["run"]:
                            print(f"{Colors.RED}{i.get('name')}: {Colors.YELLOW}{i.get('info')}")
                            
                    else:
                        print("{}Error: '{}' not exists".format(Colors.RED, arg))
                    input("")
                # ===============================
                # Only Support 1 arg.    
                # CUSTOM COMMANDS BY PLUGINS RUN:
                # ===============================
                elif len(command.split(" ")) == 2 and Custom.get(command.split(" ")[0]) is not None: 
                    error = 0
                    for i in Custom.get(command.split(" ")[0]).get("run"):
                        if i["name"] == command.split(" ")[1]:
                            try:
                                args = []
                                for k in i["fields"]:
                                    field = input(f"{k}>") 
                                    args.append(float(eval(field))) 
                                print("Converting ({})...".format(args))
                                print("""
        {}{} --> {} 
        {}   {}
                              """.format(Colors.GREEN, args[0], command.split(" ")[1], Colors.YELLOW, float(eval(str(i["return"]).replace("?", str(args[0])))))) 
                            except Exception as e:
                                print("{}Error when convertion! ({})".format(Colors.RED, command))
                                print(e)
                            error = 0
                        else:
                            error = 1
                            continue
                    if error == 1:
                        print("{}Custom command not found! ({})".format(Colors.RED, command.split(" ")[1])) 
                    input("")

                elif Types.get(command) is not None:
                    try:
                        arg = input("> ")
                        print("Converting ({})...".format(arg))
                        print("""
        {}{} --> {} 
        {}   {}
                              """.format(Colors.GREEN, arg, command, Colors.YELLOW, Types[command]["run"](arg)))
                        input("")
                    except:
                        print("{}Error when convertion! ({})".format(Colors.RED, command))
                        input("")
                elif Ms_Converters.get(command) is not None:
                    try:
                        arg = []
                        for i in Ms_Converters.get(command)["fields"]:
                            f = float(eval(input(i+": ")))
                            arg.append(f)
                        print("Converting ({})...".format(arg))
                        print("""
        {}{} --> {} 
        {}   {}
                              """.format(Colors.GREEN, arg, command, Colors.YELLOW, Ms_Converters[command]["run"](arg)))
                        input("")
                    except:
                        print("{}Error when convertion! ({})".format(Colors.RED, command))
                        input("")
                else:
                    print("{}Command not found! ({})".format(Colors.RED, command))
                    input("")
    
    def clear(self):      
        if 'nt' in os.name: 
            os.system("cls")
        else:
            os.system("clear") 
    
    def loadPlugin(self, plugin: Plugin=None):
        try:
            print(Colors.GREEN+"Loading Plugin: "+plugin.file)
            file = open(f"plugins/{plugin.file}", "r")
            
            load = json.load(file)
            
            Plugins.append(load) 
            
            print(Colors.GREEN+"Loaded successe: "+plugin.file)
        except Exception as e: 
            print(f"{Colors.RED}Error when loading plugin: {plugin.file}")
            print(e)
            
        input("")
    
class ConverterAPI:
    def __init__(self, version: int = 1):
        self.version = version
    
    def convert(self, output_type: str, input_value: any=None):
        if Types.get("apiversion") == self.version:
            return Types.get(output_type).get('run')(input_value) if Types.get(output_type) != None and output_type != "apiversion" else None
        else:
            raise Exception("Invalid API Version")
    
if __name__ == "__main__":
    main = Main()
