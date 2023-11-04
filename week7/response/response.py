from validator_collection import is_email

def main():
    email = input("What's your email address? ").strip().lower()
    if is_email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()

