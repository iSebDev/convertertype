## ConverterType

The program is a set of functions that allow conversion between different data types in Python, such as converting a string to an integer, converting a binary number to a hexadecimal number, converting a float to an integer, and many other conversion operations. Each function has a description that indicates what type of conversion it performs and how it is used. This program can be useful for anyone who needs to convert data into their Python code. ;-)

## Run in CMD to load plugins: ```python converter.py```

## Conversion Functions

| Function | Description |
| --- | --- |
| `bintohex` | Converts a binary number to hexadecimal |
| `hextobin16` | Converts a hexadecimal number to a binary number with 16 bits |
| `hextobin` | Converts a hexadecimal number to a binary number |
| `inttofloat` | Converts an integer to a float |
| `stringtohex` | Converts a string to a hexadecimal number |
| `hextostring` | Converts a hexadecimal number to a string |
| `hextoint` | Converts a hexadecimal number to an integer |
| `floattointr` | Converts a float to an integer using rounding |
| `floattoint` | Converts a float to an integer by truncating decimal points |
| `stringtobin` | Converts a string to a binary number |
| `bintoint` | Converts a binary number to an integer |
| `bintostring` | Converts a binary number to a string |
| `inttobin` | Converts an integer to a binary number |
| `inttohex` | Converts an integer to a hexadecimal number |
| `stringtob16` | Converts a string to base16 encode |
| `b16tostring` | Converts a base16 to a string |
| `stringtob64` | Converts a string to base64 encode |
| `b64tostring` | Converts a base64 to a string |
| `stringtob32` | Converts a string to base32 encode |
| `b32tostring` | Converts a base32 to a string |
| `stringtob85` | Converts a string to base85 encode |
| `b85tostring` | Converts a base85 to a string |
| `stringtob85` | Converts a string to base85 like ascii encode |
| `b85tostring` | Converts a base85 like ascii encode to a string |
| `stringtoupper` | Converts a string to upper case |
| `stringtolower` | Converts a string to lower case |
| `stringtoeval` | Converts string to value in a `eval()` (including `math.<funcs>`) |
| `hextorgb` | Convert hex color code to RGB tuple |
| `rgbtohex` | Convert RGB tuple to hex color code |
| `stringtoh256` | Encrypt an string to a hex SHA-256(unhashable) |
| `stringtoh512` | Encrypt an string to a hex SHA-512(unhashable) |
| `stringtoh1` | Encrypt an string to a hex SHA-1(unhashable) |

## Measures conversion 🎉 NEW v1.4

| Function | Description | Fields |
|------------|-------------|--------|
| mtom2      | Meters to Square Meters (x * y) | 2 |
| mmtom      | Millimeters to Meters (x/1000) | 1 |
| mtomm      | Meters to Millimeters (x*1000) | 1 |
| mtokm      | Meters to Kilometers (x/1000) | 1 |
| kmtom      | Kilometers to Meters (x*1000) | 1 |
| ltoml      | Liters to Milliliters (x * 1000) | 1 |
| mltol      | Milliliters to Liters (x / 1000) | 1 |
| gtomg      | Grams to Milligrams (x * 1000) | 1 |
| mgtog      | Milligrams to Grams (x / 1000) | 1 |

## PLUGINS ⚙️ 🎉 NEW v1.5 RELEASE

- You can make plugins in .json now 
- You can use external libs
- You can use remplazable values
- You can make extra functions for the program
- Command help : help <plugin> -> Plugin description and function names with description
- Command runfunction : <plugin_name> <function_name>
  
  # Plugin example:
  ```json
  {
    "plugin": {
        "name": "example",
        "description": "Sqrt"
    },
    "data": [
        {"name": "sqrt", "fields": ["x"], "info": "Return Squareroot of a Float", "return": "math.sqrt(?x)"},
        {"name": "sqrt2", "fields": ["x"], "info": "Return Squareroot of a Float", "return": "?x**(1/2)"},
        {"name": "sqrt3", "fields": ["x"], "depend": ["numpy"], "return": "numpy.sqrt(?x)"}
    ]
  }
  ```
