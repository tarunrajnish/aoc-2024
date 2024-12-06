def read_file_as_grid(file_path):
    grid = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Remove trailing newlines/spaces and split into characters
                grid.append(list(line.strip()))
        return grid
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    

def find_word(grid, word):
    # directions = [
    #     (-1, 0),
    #     (1, 0),
    #     (0, 1),
    #     (0, -1),
    #     (1, 1),
    #     (1, -1),
    #     (-1, 1),
    #     (-1, -1)
    # ]
    
    directions = [
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]
    
    rows, cols = len(grid), len(grid[0])
    matches = []
    
    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                if match_word(grid, word, row, col, dr, dc):
                    matches.append((row, col, dr, dc))
    return matches


def match_word(grid, word, row, col, dr, dc):
    for i in range(len(word)):
        r, c = row + i * dr, col + i * dc
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != word[i]:
            return False
    
    return True


def main():
    input_file = "input-dec-4.txt"
    
    grid = read_file_as_grid(input_file)
    # print(grid)
    
    matches = find_word(grid, "MAS")
    
    print(len(matches))
    
if __name__ == "__main__":
    main()
