def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE
    if unit_in == "c" and unit_out == "f":
        new_temp = ((9/5)*temp) + 32
        return(f"This was {temp} in Celsius and it is {new_temp} in Farenheit")
    elif unit_in =="f" and unit_out =="c":
        new_temp = (temp - 32) * (5/9)
        return(f"this was {temp} in Farenheit and it is {new_temp} in Celsius")
    elif unit_in != "c" and unit_in != "f":
        return f"invalid unit {unit_in}"
    elif unit_out != "c" and unit_out != "f":
        return f"invalid unit {unit_out}"
    elif unit_in == unit_out:
        return temp
    



print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

