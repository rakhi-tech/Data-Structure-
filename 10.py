def find_substring_occurrences(text, substring):
    positions = []
    start = 0

    while True:
        index = text.find(substring, start)  
        if index == -1:  
            break
        positions.append(index)
        start = index + 1  

    print(f"Substring '{substring}' found {len(positions)} times.")
    print("Positions:", positions)



string = input("Enter the main string: ")
sub = input("Enter the substring: ")
find_substring_occurrences(string, sub)
