#ifndef MAZEGENERATOR_H
#define MAZEGENERATOR_H

#include <cstdlib>
#include <vector>


// Maze Generator
// Reference: Wilson's Loop Erased Random Walk Algorithm

class MazeGenerator {

public:
    MazeGenerator() = default;
    MazeGenerator(int rows, int columns);
    MazeGenerator(const MazeGenerator &) = delete;
    MazeGenerator(MazeGenerator &&) = delete;
    ~MazeGenerator() = default;

    auto operator=(const MazeGenerator &) -> MazeGenerator & = delete;
    auto operator=(MazeGenerator &&) -> MazeGenerator & = delete;

    auto generate() -> std::vector<std::vector<int> >;

private:
    int m_rows = 0;
    int m_columns = 0;
    std::vector<std::vector<int> > m_maze = {{}};

    struct cell {
        int row = 0;
        int col = 0;

        auto operator==(const cell &other) const -> bool
        {
            return row == other.row && col == other.col;
        }

        auto operator<(const cell &other) const -> bool
        {
            if (row == other.row) {
                return col < other.col;
            }
            return row < other.row;
        }
    };

    void remove_wall(cell current, cell next_cell);
};

extern "C" {

struct Maze {
    int ** values;  // Array 2D
    int rows;
    int cols;
};

auto mazeGenerator(int rows, int cols) -> Maze
{
    MazeGenerator m(rows, cols);
    auto maze = m.generate();

    int ** matrix = (int**) std::malloc(rows * sizeof(int*));
    for (int r = 0; r < rows; ++r) {
        matrix[r] = (int*) std::malloc(rows * sizeof(int));
        for (int c = 0; c < cols; ++c) {
            matrix[r][c] = maze[r][c];
        }
    }

    return {matrix, rows, cols};
}

void destroy(Maze maze)
{
    for (int r = 0; r < maze.rows; ++r) {
        std::free(maze.values[r]);
    }
    std::free(maze.values);
}

}

#endif // MAZEGENERATOR_H
