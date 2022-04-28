
calculation_to_hours = 24
unitname2 = "hours"


def days_to_units(days, custom_message):
    print(f"{days} days are {days * calculation_to_hours} {unitname2}")
    print(custom_message)


days_to_units(10, "test")