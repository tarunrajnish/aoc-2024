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
    

def get_blocks_content_free_space(data):
    blocks = []
    block_counter = 0
    content = []
    free_space = []
    for d in data:
        for index, i in enumerate(d):
            # print(f"i: {i}")
            if index % 2 == 0: # they are blocks  
                # print(index)
                blocks.append(i)            
                content.append(block_counter)
                block_counter += 1
            else:
                free_space.append(i)
    
    return (blocks, content, free_space)


def get_repr(blocks, content, free_space):
    repr = []
    for index, b in enumerate(blocks):
        for i in range(int(b)):
            repr.append(content[index])
        if index != len(blocks) - 1:
            for j in range(int(free_space[index])):
                repr.append(".")
                
    return repr
    

def check_continuous(repr):
    for index, i in enumerate(repr):
        if i != ".":
            continue
        else:
            for j in range(index+1, len(repr) - 1):
                if repr[j] != ".":
                    # print("not continuous")
                    return False
                else:
                    continue
            # print("continous")
            return True

def get_checksum(repr):
    keep_going = True
    for original_index in range(len(repr) - 1, -1, -1):
        if keep_going:
            r = repr[original_index]
            # print(r)
            if r == ".":
                continue
            else:
                for index2, i in enumerate(repr):
                    if i != ".":
                        continue
                    else:
                        repr[index2] = r
                        # print(repr)
                        repr[original_index] = "."
                        # print(repr)
                        # print("---------------------------------------")
                        break
    
            if check_continuous(repr):
                keep_going = False
                
    # print(f"final repr: {repr}")

    checksum = 0
    for index, r in enumerate(repr):
        if r == ".":
            return checksum
        else:
            checksum += index * int(r)
        
    return checksum
        
def main():
    input_file = "input-dec-9-sml.txt"
    
    data = read_lines(input_file)
    # print(data)
    
    blocks, content, free_space = get_blocks_content_free_space(data)
    # print(f"blocks: {blocks}")
    # print(f"content: {content}")
    # print(f"free_space: {free_space}")
    # print(f"len blocks: {len(blocks)}")
    # print(f"len content: {len(content)}")
    # print(f"len free_space: {len(free_space)}")
    
    repr = get_repr(blocks, content, free_space)
    # print(repr)
    # print("---------------------------------------")
    checksum = get_checksum(repr)
    print(checksum)
    
    
if __name__ == "__main__":
    main()