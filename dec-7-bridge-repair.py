import itertools

def read_lines(file_path):
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


def evaluate_left_to_right(operands, operators):
    result = operands[0]  # Start with the first operand
    for i, op in enumerate(operators):
        if op == "+":
            result += operands[i + 1]  # Add the next operand
        elif op == "*":
            result *= operands[i + 1]  # Multiply the next operand
    return result

def get_valids(data):
    possible_operators = ["+", "*"]
    valid_results = set()
    
    for item in data:
        expected_value = item.split(":")[0]
        operands = item.split(":")[1].strip()
        numbers = [int(num) for num in operands.split()]
        no_operators = len(numbers) - 1
        
        print(f"expected: {expected_value}, operands: {operands}, numbers: {numbers}, no_operators:{no_operators}")
        
        operator_combinations = itertools.product(possible_operators, repeat=no_operators)

        for ops in operator_combinations:
            # print(ops)
            result = evaluate_left_to_right(numbers, ops)
            print(f"Expression: {numbers[0]} {' '.join([f'{op} {num}' for op, num in zip(ops, numbers[1:])])}, Result: {result}")
            
            if int(result) == int(expected_value):
                valid_results.add(expected_value)
        
    return valid_results

def main():
    input_file = "input-dec-7.txt"
    
    data = read_lines(input_file)
    print(data)
    
    valid_set = get_valids(data)
    
    print(valid_set)
    
    total = 0
    for item in valid_set:
        total += int(item)
        
    print(total)
    
    
if __name__ == "__main__":
    main()