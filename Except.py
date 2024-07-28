try:
    x = int(input("ENter a number: "))
    print(x)

except ValueError:
    print("Value not an input.")
else:
    print("Excellent.")
finally:
    print("Try except concept finished.")