print("Canny Controls - Quality Calculator")

process = input("Enter process name: ")
total = int(input("Enter inspected quantity: "))
rejected = int(input("Enter rejected quantity: "))

if total <= 0 or rejected < 0 or rejected > total:
    print("Invalid quantity. Please check your inputs.")
else:
    accepted = total - rejected
    rejection_percent = (rejected / total) * 100

    print("\nProcess:", process)
    print("Accepted quantity:", accepted)
    print("Rejected quantity:", rejected)
    print("Rejection percentage:", round(rejection_percent, 2), "%")