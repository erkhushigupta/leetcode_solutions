class Solution:
    def robotSim(self, commands, obstacles):
        # Define directions as (dx, dy) for north, east, south, west
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        d = 0  # 0: north, 1: east, 2: south, 3: west
        obstacle_set = set(tuple(obstacle) for obstacle in obstacles)
        max_distance = 0

        for command in commands:
            if command == -1:
                d = (d + 1) % 4
            elif command == -2:
                d = (d + 3) % 4
            else:
                for _ in range(command):
                    next_x = x + directions[d][0]
                    next_y = y + directions[d][1]
                    if (next_x, next_y) in obstacle_set:
                        break
                    x, y = next_x, next_y
                max_distance = max(max_distance, x * x + y * y)

        return max_distance
