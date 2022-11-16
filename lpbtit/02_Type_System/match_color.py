"Match was introduced in 3.10"

fav_color: str = input("Enter your favourite color:").lower()

match fav_color:
    case "black":
        print("Louis has a black t-shirt")
    case "red":
        print("Louis has a red car")
    case _:
        print(f"Louis has nothing in {fav_color}")
