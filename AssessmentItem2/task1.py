def AskUserForPositiveInteger():
    while True:
        userInput = input("Enter a positive integer (or done)")
        
        if (userInput.lower() == "done"):
            return 0
        
        try:
            userInputInteger = int(userInput)  
        except ValueError as e:
            print(f"Error: {e}")
            
        if (userInputInteger > 0):
            return userInputInteger
        print("Input was incorrect")

def main():
    integerList = []
    while True:
        userInteger = AskUserForPositiveInteger()
        if userInteger == 0:
            # user wants to see stats
            break
        integerList.append(userInteger)
            
main()