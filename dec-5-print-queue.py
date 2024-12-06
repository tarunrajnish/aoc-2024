from typing import Dict

def read_first_section(file_path):
    try:
        with open(file_path, 'r') as file:
            first_section = []
            for line in file:
                line = line.strip()
                if not line:  # Stop reading when an empty line is encountered
                    break
                first_section.append(line)
            return first_section
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def read_second_section(file_path):
    try:
        with open(file_path, 'r') as file:
            second_section = []
            found_empty_line = False
            for line in file:
                line = line.strip()
                if not line and not found_empty_line:
                    found_empty_line = True  # Start reading after the first empty line
                    continue
                if found_empty_line:
                   second_section.append([num for num in line.split(",")])
                
            return second_section
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def get_orderings(input):
    follow_dict: Dict = {}
    for item in input:
        left = item.split('|')[0]
        right = item.split('|')[1]
        
        # print(f"left: {left}, right: {right}")
        
        if left not in follow_dict:
            follow_dict[left] = [right]
        else:
            follow_dict[left].append(right)
    
    print(follow_dict)
    
    return follow_dict


def get_valid_updates(all_updates, follow_dict):
    valid_updates = []
    for update in all_updates:
        is_valid = True
        for i in range(len(update) - 1):
            for j in range(i + 1, len(update) - 1):
                if update[i] in follow_dict:
                    if update[j] not in follow_dict[update[i]]:
                        is_valid  = False
        
        
        if is_valid:
            valid_updates.append(update)
        
        
    print(valid_updates)
    

def main():
    input_file = "input-dec-5-sml.txt"
    
    first_section = read_first_section(input_file)
    print(first_section)
    
    second_section = read_second_section(input_file)
    print(second_section)
    
    follow_dict = get_orderings(first_section)
    
    valid_updates = get_valid_updates(second_section, follow_dict)

    
    
if __name__ == "__main__":
    main()
