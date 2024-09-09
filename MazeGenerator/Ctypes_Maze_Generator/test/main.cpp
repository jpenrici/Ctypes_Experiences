#include "../include/mazegenerator.hpp"

#include <iostream>
#include <print>

void view(const std::vector<std::vector<int>> &matrix)
{
    std::print("[\n");
    for (const auto &row : matrix) {
        std::print(" [");
        for (size_t i = 0; i < row.size(); ++i) {
            std::print("{:4}", row[i]);
            if (i != row.size() - 1) {
                std::print(", ");
            }
        }
        std::print("]\n");
    }
    std::print("]\n");
}

auto main() -> int
{
    try {
        std::println("Maze Generator Test ...");

        auto maze = MazeGenerator(4, 4);
        auto result = maze.generate();

        view(result);
    }
    catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << '\n';
        return 1;
    }
    catch (...) {
        std::cerr << "Error: Unknown exception.\n";
        return 1;
    }

    return 0;
}
