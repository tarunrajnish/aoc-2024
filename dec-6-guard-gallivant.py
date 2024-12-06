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


def get__initial_pos(grid, rows, cols):
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "^":
                return (r, c)


def get_count(facing_direction, pos, grid, rows, cols):
    directions = ["^", ">", "v", "<"]  # Up, Right, Down, Left
    direction_deltas = {
        "^": (-1, 0),  # Up
        ">": (0, 1),   # Right
        "v": (1, 0),   # Down
        "<": (0, -1)   # Left
    }

    def rotate_90_right(current_direction):
        # Find the next direction in clockwise order
        current_index = directions.index(current_direction)
        return directions[(current_index + 1) % len(directions)]
    
    pos_x, pos_y = pos
    visited = set()
    
    while True:
        if grid[pos_x][pos_y] != 'X':  # Add to visited only if not already 'X'
            visited.add((pos_x, pos_y))
            grid[pos_x][pos_y] = 'X'  # Mark as visited in the grid
        
        move = direction_deltas[facing_direction]
        next_x = pos_x + move[0]
        next_y = pos_y + move[1]
        
        # Check for boundaries or obstacles
        if next_x < 0 or next_x >= rows or next_y < 0 or next_y >= cols:
            print(f"Crossed boundary at: ({next_x}, {next_y})")
            return len(visited)
        
        # Allow movement to 'X' but do not add to visited
        if grid[next_x][next_y] == 'X':
            pos_x, pos_y = next_x, next_y
            print(f"Moved to: ({pos_x}, {pos_y}) - Already visited ('X')")
        
        # Check if the next position is empty and not visited
        elif grid[next_x][next_y] == "." and (next_x, next_y) not in visited:
            pos_x, pos_y = next_x, next_y
            print(f"Moved to: ({pos_x}, {pos_y})")
        
        else:
            print(f"Encountered obstacle or visited at: ({next_x}, {next_y})")
            facing_direction = rotate_90_right(facing_direction)
                

def main():
    input_file = "input-dec-6.txt"
    
    grid = read_file_as_grid(input_file)
    print(grid)
    
    rows, cols = len(grid), len(grid[0])
    print(rows, cols)
    
    initial_pos = get__initial_pos(grid, rows, cols)
    print(initial_pos)
    
    num = get_count("^", initial_pos, grid, rows, cols)
    
    print(num)
    
    
    
if __name__ == "__main__":
    main()
