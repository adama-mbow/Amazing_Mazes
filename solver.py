import amazin_maze

class LabyrinthSolver:
    def __init__(self, filename):
        self.filename = filename

    def solve_labyrinth(self):
        labyrinth = txt_to_labyrinth(self.filename)
        self.backtrack_algo(labyrinth, 0, 0)
        self.mark_solution_path(labyrinth)
        return labyrinth

    def backtrack_algo(self, laby, x, y):
        laby.board[x][y].in_way = True
        laby.board[x][y].visited = True

        if [x, y] == [laby.length - 1, laby.length - 1]:
            laby.resolve = True
            return

        case_around = case_way_possible(laby, x, y)
        if not case_around:
            laby.board[x][y].in_way = False
            return

        amazin_maze.random.shuffle(case_around)
        nx, ny = case_around[0]
        self.backtrack_algo(laby, nx, ny)

    def mark_solution_path(self, labyrinth):
        for row in labyrinth.board:
            for cell in row:
                if cell.in_way:
                    cell.content = "o"
                elif cell.visited:
                    cell.content = "*"

def main():
    filename = input("Enter the labyrinth file to solve: ")
    solver = LabyrinthSolver(filename)
    solved_labyrinth = solver.solve_labyrinth()
    
    # Print the solved labyrinth to the terminal
    for row in solved_labyrinth.board:
        print("".join(cell.content for cell in row))

if __name__ == "__main__":
    main()
