def convert_volume():
    volume = float(input("Enter the volume: "))
    print("Choose the volume type to convert:")
    print("1. Milliliters to Microliters")
    print("2. Microliters to Milliliters")
    print("3. Quarts to Gallons")
    print("4. Gallons to Quarts")
    choice = int(input("Enter your choice (1, 2, 3, or 4): "))
    if choice == 1:
        converted_volume = volume * 1000
        print(f"{volume:.2f} milliliters is equal to {converted_volume:.2f} microliters")
    elif choice == 2:
        converted_volume = volume / 1000
        print(f"{volume:.2f} microliters is equal to {converted_volume:.2f} milliliters")
    elif choice == 3:
        converted_volume = volume / 4
        print(f"{volume:.2f} quarts is equal to {converted_volume:.2f} gallons")
    elif choice == 4:
        converted_volume = volume * 4
        print(f"{volume:.2f} gallons is equal to {converted_volume:.2f} quarts")
    else:
        print("Invalid choice")

convert_volume()
