def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
    # Define variables for the first 2 characters and last characters
    lead_char = s[:2]
    out_char = s[2:]
    
    # Validate all required conditions to be True
    if len(s) >= 2 and len(s) <= 6:
        if s.isalnum():
            if lead_char.isalpha():
                for i in range(len(out_char)):
                    if out_char[i] == "0":
                        return False
                        break
                    elif out_char[i].isdigit():
                        if out_char[i:].isdigit():
                            return True
                        else:
                            return False
                            break
                    else:
                        #return True
                        continue
                return True
    else:
        return False

main()