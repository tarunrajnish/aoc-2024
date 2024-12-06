def process_input(file_path):
    """
    Reads and processes the content of the input file.

    Args:
        file_path (str): Path to the input file.

    Returns:
        list: Processed data from the file.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.readlines()
        processed_data = [line.strip() for line in data]
        return processed_data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def check_safety(line) -> bool:
    # Clean the input: remove spaces and split into integers
    cleaned_line = [int(x) for x in line.split() if x.strip().isdigit()]
    # print("Cleaned Line:", cleaned_line)
    
    bad_count_1 = 0
    bad_count_2 = 0
            
    for i in range(len(cleaned_line) - 1):
        element1 = cleaned_line[i]
        element2 = cleaned_line[i + 1]
        
        # print(f"Comparing {element1} and {element2}")
       
        # Add your comparison logic here
        if abs(element1 - element2) < 1 or abs(element1 - element2) > 3:
            if bad_count_1 == 0:
                bad_count_1 = 1
            else: 
                return False 
        
        if not all(cleaned_line[i] < cleaned_line[i + 1] for i in range(len(cleaned_line) - 1)) and not all(cleaned_line[i] > cleaned_line[i + 1] for i in range(len(cleaned_line) - 1)):
            if bad_count_2 == 0:
                bad_count_2 = 1
            else: 
                return False 

    return True
    
def main():
    input_file = "input-dec-2.txt"
    
    data = process_input(input_file)
    
    if data: 
        num_safe = 0
        for i, line in enumerate(data, 1):
            is_safe = check_safety(line)
            if is_safe:
                num_safe += 1
                
        print(num_safe)
            
        
    else:
        print("No data to process.")

if __name__ == "__main__":
    main()
