def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return

    except Exception as v:
        print(v)
        return

    finally:
        print("I am inside finally")

main()