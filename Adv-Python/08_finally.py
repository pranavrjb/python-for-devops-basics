def main():
    try:
        a=int(input("Enter the number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return
        
    finally:
        print("Hey, I am inside of Finally")

main()