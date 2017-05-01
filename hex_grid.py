def min_grid_path(grid, x, y):
    cost_matrix = [[0 for _ in range(x+1)] for _ in range(y+1)]

    cost_matrix[0][0] = grid[0][0]

    # initialize by sum in 1st column
    for i in range(1, x+1):
        cost_matrix[i][0] = hex_sum(cost_matrix[i-1][0], grid[i][0])

    # initialize by sum in 1st row
    for i in range(1, y+1):
        cost_matrix[0][i] = hex_sum(cost_matrix[0][i-1], grid[0][i])

    # building cost matrix bottom up
    for i in range(1, x+1):
        for j in range(1, y+1):
            cost_matrix[i][j] = hex_sum(
                            hex_min(cost_matrix[i-1][j], cost_matrix[i][j-1]),
                            grid[i][j])

    # iterate over cost matrix and find least cost path
    path = []
    i = x
    j = y
    while not(i == 0 and j == 0):
        m = hex_min(cost_matrix[i-1][j], cost_matrix[i][j-1])
        if m == cost_matrix[i-1][j]:
            path.append('d')
            i -= 1
        else:
            path.append('r')
            j -= 1
    return path[::-1]


if __name__ == '__main__':
    grid = [['46B', 'E59', 'EA', 'C1F', '45E', '63'],
            ['899', 'FFF', '926', '7AD', 'C4E', 'FFF'],
            ['E2E', '323', '6D2', '976', '83F', 'C96'],
            ['9E9', 'A8B', '9C1', '461', 'F74', 'D05'],
            ['EDD', 'E94', '5F4', 'D1D', 'D03', 'DE3'],
            ['89', '925', 'CF9', 'CA0', 'F18', '4D2']]
    hex_sum = lambda x, y: hex(int('0x'+x, 16) + int('0x'+y, 16))[2:]
    hex_min = lambda x, y: x if int('0x'+x, 16) < int('0x'+y, 16) else y

    path = min_grid_path(grid, 5, 5)
    print ' '.join(path)

""""
def min_grid_recursive(grid, x, y):
    if x < 0 or y < 0:
        return 'f423f'
    elif x == 0 and y == 0:
        return grid[x][y]
    else:
        return hex_sum(grid[x][y], hex_min(min_grid_recursive(grid, x-1, y),
                                           min_grid_recursive(grid, x, y-1)))
"""
