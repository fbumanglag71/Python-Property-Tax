## Author: Francisco Bumanglag
## Project: Property Tax
## Assignment: Module 2 Project 4
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 24, 2023


def calculations(actual_value):
    
    assessment_value = 0.6 * actual_value               #60% of actual value
    property_tax = (assessment_value / 100) * 0.72      #72¢ for each $100 of assessment value\
    return assessment_value, property_tax               #pass the variables to def main()


def main():
    #user input -- get the actual value of the property
    actual_value = float(input("Enter the actual value of the property: "))

    #call the function "calculations" to calculate assessment value and property tax
    assessment_value, property_tax = calculations(actual_value)
  
    #display the assessment value and property tax
    print(f"Assessment value is: ${assessment_value:,.2f}")
    print(f"Property tax is: ${property_tax:,.2f}" )


# Call the main function to start the program
main()
