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
    
def find_total_distance(list1, list2):
    total = 0
    
    for i, (item1, item2) in enumerate(zip(list1, list2), 1):
        # print(f"{i}: {item1} {item2}")
        diff = abs(int(item1)-int(item2))
        total += diff
    
    print(total)
    
def find_similarity_score(list1, list2):
    total = 0
    
    for i in list1:
        counter = 0
        for j in list2:
            if int(i) == int(j):
                counter += 1
        similarity = int(i) * counter
        total += similarity
    
    print(total)
    
def main():
    input_file = "input-dec-1.txt"
    
    data = process_input(input_file)
    
    if data:
        list1 = []  # To store first elements
        list2 = []  # To store second elements
        
        print("Processed Data:")
        for i, line in enumerate(data, 1):
            # Split the line on space and remove any extra spaces
            elements = [x.strip() for x in line.split() if x.strip()]
            
            # Ensure there are at least two elements before proceeding
            if len(elements) >= 2:
                list1.append(elements[0])
                list2.append(elements[1])
            
            # print(f"{i}: {elements}")
        
        # print("\nList 1:", list1)
        # print("List 2:", list2)
        
        print("len of list1: ", len(list1))
        print("len of list2: ", len(list2))
        
        list1.sort()
        list2.sort()
        
        find_total_distance(list1, list2)
        find_similarity_score(list1, list2)
        
    else:
        print("No data to process.")

if __name__ == "__main__":
    main()
