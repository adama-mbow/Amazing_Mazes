import random

class Generateurlabyrinth:
    def __init__(self, n):
        self.n = n
        self.labyrinth = [[1] * n for _ in range(n)]

    def is_valid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n

    def mark_visited(self, x, y):
        self.labyrinth[y][x] = 0

    def recursive_backtracking(self, x, y):
        self.mark_visited(x, y)

        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny) and self.labyrinth[ny][nx] == 1:
                self.labyrinth[y + dy // 2][x + dx // 2] = 0
                self.recursive_backtracking(nx, ny)

    def generate_labyrinth(self):
        self.recursive_backtracking(0, 0)

class LabyrinthFileWriter:
    def __init__(self, labyrinth, filename):
        self.labyrinth = labyrinth
        self.filename = filename

    def write_to_file(self):
        with open(self.filename, 'w') as file:
            for row in self.labyrinth:
                file.write("".join(["#" if cell == 1 else "." for cell in row]) + '\n')

def main():
    n = int(input("Entrez la taille du labyrinthe (n*n) : "))
    filename = input("Entrez le nom du fichier de sortie : ")

    generator = Generateurlabyrinth(n)
    generator.generate_labyrinth()

    writer = LabyrinthFileWriter(generator.labyrinth, filename)
    writer.write_to_file()

if __name__ == "__main__":
    main()
