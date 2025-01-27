make = input("Enter Make: ")
model = input("Enter Model: ")
year = int(input("Enter Year: "))
start = int(input("Enter Starting Mileage: "))
end = int(input("Enter End Mileage: "))
mpg = float(input("Average MPG of Vehicle: "))
car = {
    "make": make,
    "model": model,
    "year": year,
    "start_miles": start,
    "end_miles": end,
    "avg_mpg": mpg
    }


print(car)
