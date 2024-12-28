import math

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


def get_distanct_dict(grid, rows, cols):
    dist_dict = {}
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.':
                continue
            else:
                if grid[r][c] not in dist_dict.keys():
                    dist_dict[grid[r][c]] = [(r, c)]
                else:
                    dist_dict[grid[r][c]].append((r, c))           
            
    print(dist_dict)
    
    return dist_dict
    
def get_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def find_antinodes(grid, rows, cols, dist_dict):
    print(dist_dict)
    antinodes = {}
    
    for symbol, coords in dist_dict.items():
        if len(coords) < 2:
            continue  # Skip symbols with fewer than two appearances
        
        print(f"Processing symbol: {symbol}")
        antinodes[symbol] = []
        
        # Calculate distances and antinodes for each pair
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                p1 = coords[i]
                p2 = coords[j]
                
                # Calculate distance
                distance = get_distance(p1, p2)
                print(f"Points: {p1}, {p2}, Distance: {distance}")
                
                # Calculate midpoint
                midpoint = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
                print(f"Midpoint: {midpoint}")
                
                # Find antinodes on the grid (equidistant from p1 and p2)
                for r in range(rows):
                    for c in range(cols):
                        if (r, c) != p1 and (r, c) != p2 and grid[r][c] == ".":
                            d1 = get_distance((r, c), p1)
                            d2 = get_distance((r, c), p2)
                            if math.isclose(d1, d2, rel_tol=1e-6):  # Check equidistance
                                antinodes[symbol].append((r, c))
                                print(f"Antinode found at: ({r}, {c})")
    
    return antinodes  
            
def main():
    input_file = "input-dec-8-sml.txt"
    
    grid = read_file_as_grid(input_file)
    print(grid)
    
    rows, cols = len(grid), len(grid[0])
    print(rows, cols)
    
    dist_dict = get_distanct_dict(grid, rows, cols)
    
    antinodes = find_antinodes(grid, rows, cols, dist_dict)
    print(antinodes)
    
    
if __name__ == "__main__":
    main()
