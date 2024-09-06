#ifndef MAZEGENERATOR_H
#define MAZEGENERATOR_H

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

// TO DO

struct maze {
    int ** values;
    int rows;
    int cols;
};

auto mazeGenerator(int rows, int cols) -> maze
{
    MazeGenerator m(rows, cols);
    auto matrix = m.generate();

    int arr[rows][cols];

    return {arr, rows, cols};
}

}

#endif // MAZEGENERATOR_H
