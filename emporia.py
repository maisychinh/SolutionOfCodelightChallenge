import sys
# Function for dfs.
# i, j ==> Current cell indexes
# vis ==> To mark visited cells
# ans ==> Result
# z ==> Current count 0s visited
# z_count ==> Total 0s present
def DFStraverse(i, j, grid, vis, ans, z, z_count):
    n = len(grid)
    m = len(grid[0])

    # Mark the block as visited
    vis[i][j] = 1

    if (grid[i][j] == 0):
        # Update the count
        z += 1

    # If end block reached
    if (grid[i][j] == 3):

        # If path covered all the non-
        # obstacle blocks
        if (z == z_count):
            ans += 1

        vis[i][j] = 0

        return grid, vis, ans

    # Up
    if (i >= 1 and not vis[i - 1][j] and
            grid[i - 1][j] != 1):
        grid, vis, ans = DFStraverse(i - 1, j, grid,
                             vis, ans, z,
                             z_count)

    # Down
    if (i < n - 1 and not vis[i + 1][j] and
            grid[i + 1][j] != 1):
        grid, vis, ans = DFStraverse(i + 1, j, grid,
                             vis, ans, z,
                             z_count)

    # Left
    if (j >= 1 and not vis[i][j - 1] and
            grid[i][j - 1] != 1):
        grid, vis, ans = DFStraverse(i, j - 1, grid,
                             vis, ans, z,
                             z_count)

    # Right
    if (j < m - 1 and not vis[i][j + 1] and
            grid[i][j + 1] != 1):
        grid, vis, ans = DFStraverse(i, j + 1, grid,
                             vis, ans, z,
                             z_count)

    # Unmark the block (unvisited)
    vis[i][j] = 0

    return grid, vis, ans


# Function to return the count
# of the unique paths
def CalNumOfUniquePaths(grid):
    # Total 0s present
    z_count = 0
    n = len(grid)
    m = len(grid[0])
    ans = 0

    vis = [[0 for j in range(m)]
           for i in range(n)]

    x = 0
    y = 0

    for i in range(n):
        for j in range(m):

            # Count non-obstacle blocks
            if grid[i][j] == 0:
                z_count += 1

            elif (grid[i][j] == 2):

                # Starting position
                x = i
                y = j

    grid, vis, ans = DFStraverse(x, y, grid,
                         vis, ans, 0,
                         z_count)

    return ans


# Driver code
if __name__ == '__main__':
    grid = []
    # Read the firstLine that includes size of the grid
    firstLine = sys.stdin.readline()
    sizeArr = [int(elem) for elem in firstLine.split()]
    # Get num of rows and columns
    row = sizeArr[0]
    col = sizeArr[1]
    # Read next lines to get grid
    for i in range(row):
        line = sys.stdin.readline()
        rowArr = [int(elem) for elem in line.split()]
        grid.append(rowArr)
    # Print num of unique paths
    print(CalNumOfUniquePaths(grid))
