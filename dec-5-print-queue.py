from typing import Dict
import math

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


def get_forward_lookup(input):
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


def get_backward_lookup(input):
    follow_dict: Dict = {}
    for item in input:
        left = item.split('|')[0]
        right = item.split('|')[1]
        
        # print(f"left: {left}, right: {right}")
        
        if right not in follow_dict:
            follow_dict[right] = [left]
        else:
            follow_dict[right].append(left)
    
    print(follow_dict)
    
    return follow_dict


def get_valid_updates(all_updates, forward_dict, backward_dict):
    valid_updates = []
    invalid_updates = []
    
    for update in all_updates:
        is_valid = True
        for i in range(len(update)):
            for j in range(len(update)):
                if i == j:
                    continue
                elif i < j:
                    if update[i] in forward_dict.keys() and update[j] not in forward_dict[update[i]]:
                        is_valid = False
                else:
                    if update[i] in backward_dict.keys() and update[j] not in backward_dict[update[i]]:
                        is_valid = False
        
        if is_valid:
            valid_updates.append(update)
                     
    print(valid_updates)
    return valid_updates
    

def main():
    input_file = "input-dec-5.txt"
    
    first_section = read_first_section(input_file)
    print(first_section)
    
    second_section = read_second_section(input_file)
    print(second_section)
    
    forward_dict = get_forward_lookup(first_section)
    backward_dict = get_backward_lookup(first_section)
    
    valid_updates = get_valid_updates(second_section, forward_dict, backward_dict)

    sum_middle = 0
    
    for update in valid_updates:
        size = len(update)
        middle_index = math.floor(size / 2)
        print(middle_index)
        
        sum_middle += int(update[middle_index])
        
    print(sum_middle)
    
if __name__ == "__main__":
    main()
