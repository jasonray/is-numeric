# is-numeric

Really simple.  A method to test if a value `is_numeric`.

``` python 
from is_numeric import is_numeric
print( is_numeric(1) )           # True
print( is_numeric(-1) )          # True
print( is_numeric(123) )         # True
print( is_numeric(123.456) )     # True
print( is_numeric("123.456") )   # True
print( is_numeric("x") )         # False
print( is_numeric("1x") )        # False
```

# Installation

```
pip install is-numeric
```

# Notes on the algorithm

I tested 4 algorithms:
* str.isinstance
* error-driven
* regex
* regex (plus str.isinstance)

## str.isinstance

Using the built in .isinstance is limited in functionality, as it only looks for all characters being a digit, and fails on '-1' or '1.2'.  Thus discard this approach.

```
def _str_isnumeric(value):
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, str) and value.isnumeric():
        return True
    return False
```

## error-driven

This is ugly in that it relies on errors in flow control.  I hate it.  It is like nails on chalk board to me.

```
def _is_numeric_using_error(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
```

## regex

This seems elegant.  Check for a pattern.

```
def _is_numeric_regex(value):
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, str):
        return bool(re.match(r"^-?\d+(\.\d+)?$", value))
    return False
```

## regex (plus str.isinstance)

The regex solution, with a small change to check if all numeric digits prior to doing regex.

```
def _is_numeric_regex_plus_isnumeric(value):
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, str) and value.isnumeric():
        return True
    if isinstance(value, str):
        return bool(re.match(r"^-?\d+(\.\d+)?$", value))
    return False
```

## Performance Comparison

I ran a very non-scientific test.

**Approach**
Create a list of inputs, with a mix of float/int, strings that represent numeric values, and non-numeric values.
Iterate x time over the list for a given algorithm.
Repeat for each algorithm.

**Variable**
* % of inputs that are non-numeric (theory is that error-driven will perform better when the value is numeric, and less efficient when the value cannot be cast to float and an error is raised)

**Findings**
When most values are numeric [^1] (0-50%), the error-driven approach outperforms other approaches (up to 3x).  
When most values are non-numeric [^2] (80%), the regex (plus str.isinstance) approach has a very slight advantage (4%).

**Conclusion**
without knowning the % of non-numeric values, it is recommended to use the error-driven approach.  As such, the error-drive approach is exposed through the `is_numeric` function in this package.


### Raw Data
const: iterations=1000000

| Algorithm                           | % Non-Numeric | Time in Seconds | Iterations per Second |
|-------------------------------------|---------------|-----------------|-----------------------|
| is_numeric_regex_plus_isnumeric     | 0.0           | 4.176071        | 239,459.52            |
| is_numeric_using_error              | 0.0           | 1.469144        | 680,668.39            |
| is_numeric_regex                    | 0.0           | 4.719131        | 211,903.44            |
| is_numeric_regex_plus_isnumeric     | 0.2           | 5.893955        | 169,665.37            |
| is_numeric_using_error              | 0.2           | 3.295613        | 303,433.65            |
| is_numeric_regex                    | 0.2           | 6.379531        | 156,751.32            |
| is_numeric_regex_plus_isnumeric     | 0.5           | 10.687538       | 93,566.92             |
| is_numeric_using_error              | 0.5           | 8.338870        | 119,920.32            |
| is_numeric_regex                    | 0.5           | 10.848000       | 92,182.89             |
| is_numeric_regex_plus_isnumeric     | 0.8           | 29.750488       | 33,612.89             |
| is_numeric_using_error              | 0.8           | 28.508906       | 35,076.76             |
| is_numeric_regex                    | 0.8           | 28.439334       | 35,162.57             |

[^1]: numeric = float/int, strings that represent numeric values
[^2]: non-numeric = strings that cannot be cast to float/int
