class InvalidVoterException(Exception):
    pass

age = int(input("Enter your age: "))
try:
    if age < 18:
        raise InvalidVoterException("Age is less than 18. Invalid voter.")
    print("You are eligible to vote.")
except InvalidVoterException as e:
    print(e)
