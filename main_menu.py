def menu():
    print("\nJenkins Job Manager Main Menu:")
    define = (f"Jenkins Job Manager Main Menu:")
    print("=" * len(define))
    print()
    print("1. Add jobs")
    print("2. Delete jobs")
    print("3. Update jobs")
    print("4. Load demi data, Comming soon")
    print("5. Display jobs")
    print("6. Exit the app")
    
    choice = input("\nSelect an option (1-6): ")
    return choice