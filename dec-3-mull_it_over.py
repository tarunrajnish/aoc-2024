import re
index = 0
def get_buffer(file_path, flag):
    if flag:
        pattern = r"don't\(\)"
    else:
        pattern = r"do\(\)"
    
    buffer = ""
    
    try:
        with open(file_path, 'r') as file:
            # content = file.read()  # Read the entire file content
            while True:
                char = file.read(1)  # Read one character at a time
                if not char:  # End of file
                    break
                
                buffer += char  # Add the character to the buffer

                # Check if the buffer contains the pattern
                match = re.search(pattern, buffer)
                if match:
                    return buffer  # Return the first match immediately

        return None  # Return None if no match is found
             
        # Use regex to find all matches
        # patterns = re.findall(r"mul\(\d+,\d+\)", content)
        # return patterns
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
    
def main():
    input_file = "input-dec-3.txt"
    total = 0
    
    do_flag = True
    buffer = get_buffer(input_file, do_flag)
    
    print(buffer)
    if do_flag:
        print(f"We have to multiply: {buffer}")
        
        for item in buffer:
            match = re.match(r"mul\((\d+),(\d+)\)", item)
            if match:
                num1 = int(match.group(1))  # First number
                num2 = int(match.group(2))  # Second number
                product = num1 * num2
                # print(f"Numbers: {num1}, {num2} -> Product: {product}")
                
                total += product
        
        print(total)
        do_flag = False
        
    else:
        print("Pattern not found.")
   

if __name__ == "__main__":
    main()
