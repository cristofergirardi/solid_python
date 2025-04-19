def calculate_shipping_cost(weight, carrier):
    cost = 0
    if carrier == "FedEx":
        cost = weight * 2.5
    elif carrier == "UPS":
        cost = weight * 3
    elif carrier == "DHL":
        cost = weight * 4
    return cost

print("Select a carrier for shipping:")
print("1. FedEx")
print("2. UPS")
print("3. DHL")

choice = int(input("Enter the number corresponding to your choice: "))
weight = float(input("Enter the weight of the package (in pounds): "))

if choice == 1:
    carrier = "FedEx"
elif choice == 2:
    carrier = "UPS"
elif choice == 3:
    carrier = "DHL"
else:
    print("Invalid choice!")
    exit(1)

shipping_cost = calculate_shipping_cost(weight, carrier)
print(f"The shipping cost for {carrier} is ${shipping_cost:.2f}")