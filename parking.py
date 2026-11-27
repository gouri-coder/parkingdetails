vehicle_type = input("Enter vehicle type(Two wheeler/Four wheeler/Heavy vehicle):")
hours = float(input("Enter parking duration in hours:"))

if vehicle_type =="Two-wheeler":
    rate = 20

    if vehicle_type =="Four-wheeler":
        rate = 50

        if vehicle_type =="Heavy-vehicle":
            rate = 100

        else:
            rate = 0
            print("Invalid vehicle type entered")
            total_fee = rate*hours

            if rate>0:
                print("\n---Parking receipt---")
                print(f"vehicle type  :{vehicle_type.title()}")

                print(f"Parking Duration :{hours}hours")
                print(f"Total Parkig Fee :Rs{total_fee}")