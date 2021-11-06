print("Hello class")
print("The variable __name__ tells me which context this file is running in.")
print("The value of __name__ is:", repr(__name__))

class Query():
    pass

class Database():
    pass

def main():
    print("Hello in main!")

if __name__ == "__main__":
    main()