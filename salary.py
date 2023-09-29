# Take qty and price and display amount after 10% discount

salary = int(input("Enter salary :"))

if salary > 50000:
    HRA = salary * 25 // 100
    print(f"HRA       :{HRA:6}")
    DA = salary * 15 // 100
    print(f"DA        :{DA:6}")
    print(f"Salary    :{salary:6}")
    net = salary-(HRA+DA)
    print(f"Net Salary:{net:6}")
else:
    HRA = salary * 20 // 100
    print(f"HRA       :{HRA:6}")
    DA = salary * 12 // 100
    print(f"DA        :{DA:6}")
    print(f"Salary    :{salary:6}")
    net = salary - (HRA + DA)
    print(f"Net Salary:{net:6}")
