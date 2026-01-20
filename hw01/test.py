"""Performs Tests on Functions"""

from conversion import (
    pound_to_kilogram, kilogram_to_pound,
    fahrenheit_to_celsius, celsius_to_fahrenheit,
    feet_to_meters, meters_to_feet,
    acres_to_square_feet, square_feet_to_acres, what_function
)
def test_pound_to_kilogram():
    """Tests pounds to kilograms."""
    assert pound_to_kilogram(10) == 4.54
    assert pound_to_kilogram(50) == 22.68
    assert pound_to_kilogram(123) == 55.78
    assert pound_to_kilogram(1) == 0.45
    assert pound_to_kilogram(1000) == 453.51
    assert pound_to_kilogram(0) == 0.0
    assert pound_to_kilogram(-10) == -4.54
    assert pound_to_kilogram(3456) == 1567.35
    assert pound_to_kilogram(123456789) == 55989473.47
    assert pound_to_kilogram(300) == 136.05

def test_kilogram_to_pound():
    """Tests kilograms to pounds."""
    assert kilogram_to_pound(1) == 2.21
    assert kilogram_to_pound(5) == 11.03
    assert kilogram_to_pound(10) == 22.05
    assert kilogram_to_pound(50) == 110.25
    assert kilogram_to_pound(100) == 220.5
    assert kilogram_to_pound(0) == 0.0
    assert kilogram_to_pound(-5) == -11.03
    assert kilogram_to_pound(0.45) == 0.99
    assert kilogram_to_pound(20) == 44.1
    assert kilogram_to_pound(75) == 165.38

def test_fahrenheit_to_celsius():
    """Tests Fahrenheit to Celsius."""
    assert fahrenheit_to_celsius(32) == 0.0
    assert fahrenheit_to_celsius(212) == 100.0
    assert fahrenheit_to_celsius(98.6) == 37.0
    assert fahrenheit_to_celsius(-40) == -40.0
    assert fahrenheit_to_celsius(0) == -17.78
    assert fahrenheit_to_celsius(451) == 232.78
    assert fahrenheit_to_celsius(100) == 37.78
    assert fahrenheit_to_celsius(50) == 10.0
    assert fahrenheit_to_celsius(-10) == -23.33
    assert fahrenheit_to_celsius(300) == 148.89

def test_celsius_to_fahrenheit():
    """Tests Celsius to Fahrenheit."""
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(37) == 98.6
    assert celsius_to_fahrenheit(-40) == -40.0
    assert celsius_to_fahrenheit(20) == 68.0
    assert celsius_to_fahrenheit(-10) == 14.0
    assert celsius_to_fahrenheit(50) == 122.0
    assert celsius_to_fahrenheit(10) == 50.0
    assert celsius_to_fahrenheit(25) == 77.0
    assert celsius_to_fahrenheit(200) == 392.0

def test_feet_to_meters():
    """Tests feet to meters."""
    assert feet_to_meters(10) == 3.05
    assert feet_to_meters(50) == 15.24
    assert feet_to_meters(0) == 0.0
    assert feet_to_meters(100) == 30.48
    assert feet_to_meters(1) == 0.30
    assert feet_to_meters(3) == 0.91
    assert feet_to_meters(500) == 152.39
    assert feet_to_meters(1000) == 304.79
    assert feet_to_meters(-10) == -3.05
    assert feet_to_meters(25) == 7.62

def test_meters_to_feet():
    """Tests meters to feet."""
    assert meters_to_feet(10) == 32.81
    assert meters_to_feet(50) == 164.05
    assert meters_to_feet(0) == 0.0
    assert meters_to_feet(1) == 3.28
    assert meters_to_feet(100) == 328.1
    assert meters_to_feet(3) == 9.84
    assert meters_to_feet(0.5) == 1.64
    assert meters_to_feet(1000) == 3281.00
    assert meters_to_feet(-10) == -32.81
    assert meters_to_feet(25) == 82.03

def test_acres_to_square_feet():
    """Tests acres to square feet."""
    assert acres_to_square_feet(1) == 43560
    assert acres_to_square_feet(10) == 435600
    assert acres_to_square_feet(0) == 0
    assert acres_to_square_feet(0.5) == 21780
    assert acres_to_square_feet(5) == 217800
    assert acres_to_square_feet(25) == 1089000
    assert acres_to_square_feet(50) == 2178000
    assert acres_to_square_feet(75) == 3267000
    assert acres_to_square_feet(100) == 4356000
    assert acres_to_square_feet(200) == 8712000

def test_square_feet_to_acres():
    """Tests square feet to acres."""
    assert square_feet_to_acres(43560) == 1.0
    assert square_feet_to_acres(87120) == 2.0
    assert square_feet_to_acres(0) == 0.0
    assert square_feet_to_acres(21780) == 0.5
    assert square_feet_to_acres(435600) == 10.0
    assert square_feet_to_acres(100000) == 2.295684
    assert square_feet_to_acres(5000) == 0.114784
    assert square_feet_to_acres(200000) == 4.591368
    assert square_feet_to_acres(15000) == 0.344353
    assert square_feet_to_acres(300000) == 6.887052

def test_what_function():
    """Tests what function"""
    assert what_function("10 lbs") == 4.54
    assert what_function("5 kg") == 11.03
    assert what_function("32 F") == 0.0
    assert what_function("0 C") == 32.0
    assert what_function("50 ft") == 15.24
    assert what_function("10 m") == 32.81
    assert what_function("2 ac") == 87120
    assert what_function("43560 sqft") == 1.0
    assert what_function("0 lbs") == 0.0
    assert what_function("0 ft") == 0.0
