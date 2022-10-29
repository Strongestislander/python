
# Dictionaries have to use {}
month_conversion = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}
print("This script will grab a month in long format")
print("Please input a month in short form")
print("Please Capitalize the first letter")
print("----------------------------------")
user_in = input("input month: ")

# get lets user variable in the dictionary
print(month_conversion.get(user_in, "Not a valid month"))