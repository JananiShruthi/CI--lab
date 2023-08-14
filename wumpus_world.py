def update_grid(grid, size, i, j, action):
    if((i+1)%size == (i+1)):#next row same column
        if(grid[i+1][j] == '0'):
            grid[i+1][j] = action
        else:
            grid[i+1][j] += action
    if((j+1)%size == (j+1)):#Same row next column
        if(grid[i][j+1] == '0'):
            grid[i][j+1] = action
        else:
            grid[i][j+1] += action
    if(i != 0):
        if(grid[i-1][j] == '0'):
            grid[i-1][j] = action#previous row same column
        else:
            grid[i-1][j] += action
    if(j != 0):
        if(grid[i][j-1] == '0'):       
            grid[i][j-1] = action
        else:
            grid[i][j-1] += action

def is_valid(x, y, size):
    return 0 <= x < size and 0 <= y < size

def test_P(s):
    for i in s:
        if i == 'P':
            return True
    return False
    
def test_W(s):
    for i in s:
        if i == 'W':
            return True
    return False

def test_G(s):
    for i in s:
        if i == 'G':
            return True
    return False

def dfs(start_x, start_y, visited, path, grid):
    if not is_valid(start_x, start_y, size) or visited[start_x][start_y] or test_P(grid[start_x][start_y]) or test_W(grid[start_x][start_y]):
        return False
    visited[start_x][start_y] = True
    path.append((start_x, start_y))
    
    if (test_G(grid[start_x][start_y])):
        return True
    
    if dfs(start_x + 1, start_y, visited, path, grid) or dfs(start_x - 1, start_y, visited, path, grid) or dfs(start_x, start_y + 1, visited, path, grid) or dfs(start_x, start_y - 1, visited, path, grid):
        return True

    path.pop() #used to backtrack and remove the last added cell from the path when the algorithm determines that the current path is not leading to the goal.
    return False

def find_path(grid, size, start_x, start_y):
    visited = [[False] * size for _ in range(size)]
    path = []
    if(dfs(start_x, start_y, visited, path, grid)):
        return path
    else:
        return None
    

size = int(input("Enter the world size: "))
grid = [['0'] * size for _ in range(size)]

x, y = input("Enter the wumpus position: ").split()
w_x = int(x)
w_y = int(y)
grid[w_x][w_y] = 'W'

update_grid(grid, size, w_x, w_y, 'S')

pits = int(input("Enter the number of pits for the grid: "))
for i in range(pits):
    pitx, pity = input("Enter the pit position: ").split()
    grid[int(pitx)][int(pity)] = 'P'

print(grid)

for i in range(size):
    for j in range(size):
        if grid[i][j] == 'P':
            update_grid(grid, size, i, j, 'B')

x, y = input("Enter the Goal position: ").split()
g_x = int(x)
g_y = int(y)
if(grid[g_x][g_y] != '0'):
    grid[g_x][g_y] += 'G'
else:
    grid[g_x][g_y] = 'G'

print(grid)

x, y = input("Enter the start position: ").split()
start_x = int(x)
start_y = int(y)
path = find_path(grid, size, start_x, start_y)

if path != 'None':
    print("The path to reach the goal is: ", path)
else:
    print("No path exist")