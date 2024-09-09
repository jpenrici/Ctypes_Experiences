#include "../include/mazegenerator.hpp"

#include <algorithm>
#include <array>
#include <random>
#include <set>
#include <vector>

// Maze Generator
// Reference: Wilson's Loop Erased Random Walk Algorithm

MazeGenerator::MazeGenerator(int rows, int columns) :
    m_rows(rows),
    m_columns(columns),
    m_maze(std::vector<std::vector<int> >(rows, std::vector<int>(columns, 0)))
{
    // Maze is a two-dimensional list where the binary flag represents:
    // 0: All walls closed.
    // 1: Left wall open.
    // 2: Bottom wall open.
    // 4: Right wall open.
    // 8: Top wall open.
    // 6 (2 + 4): Right wall and bottom wall open.
    // 9 (8 + 1): Top wall and left wall open.
    // 10 (8 + 2): Top wall and bottom wall open.
    // 12 (8 + 4): Top wall and right wall open.
    //
    // Detail:
    // 0000 : Zero (Closed), One (Open)
    // ||||__ Left Wall
    // |||___ Bottom Wall
    // ||____ Right Wall
    // |_____ Top Wall
}

auto MazeGenerator::generate() -> std::vector<std::vector<int> >
{
    // Controllers.
    std::set<cell> visited;
    auto size = m_rows * m_columns;
    std::vector<cell> unvisited(size);

    // Directions: {row_offset, col_offset} for right, down, left, up.
    std::vector<std::array<int, 2>> directions{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    // Initialize.
    for (int r = 0; r < m_rows; ++r) {
        for (int c = 0; c < m_columns; ++c) {
            unvisited[r * m_columns + c] = {r, c};
        }
    }

    std::random_device rd;
    std::mt19937 gen(rd());
    std::shuffle(unvisited.begin(), unvisited.end(), gen);

    auto current = unvisited.back();
    visited.insert(current);
    unvisited.pop_back();

    // Build.
    while (!unvisited.empty()) {
        std::vector<cell> path;
        auto start = unvisited.back();

        // Walk.
        while (visited.find(start) == visited.end()) {
            path.push_back(start);
            std::uniform_int_distribution<> dist(0, static_cast<int>(directions.size() - 1));
            std::array<int, 2> direction = directions.at(dist(gen));
            auto next_cell = cell{start.row + direction.front(), start.col + direction.back()};

            if (next_cell.row >= 0 && next_cell.row < m_rows && next_cell.col >= 0 && next_cell.col < m_columns) {
                // Update cell.
                start = next_cell;
            }
            else if (!path.empty()) {
                // Protect the boundaries.
                start = path.back();
                path.pop_back();
            }

            auto it = std::find(path.begin(), path.end(), start);
            if (it != path.end()) {
                // Remove loop.
                path.resize(it - path.begin() + 1);
            }
        }

        // Update and clean.
        for (const auto &cell : path) {
            unvisited.erase(std::remove(unvisited.begin(), unvisited.end(), cell), unvisited.end());
            visited.insert(cell);
        }

        // Remove walls.
        for (size_t i = 0; i < path.size() - 1; ++i) {
            remove_wall(path[i], path[i + 1]);
        }
    }

    return m_maze;
}

void MazeGenerator::remove_wall(cell current_cell, cell next_cell)
{
    auto row_diff = next_cell.row - current_cell.row;
    auto col_diff = next_cell.col - current_cell.col;

    if (row_diff == 1) {
        m_maze[current_cell.row][current_cell.col] |= 2;    // 0010 : Remove bottom wall
        m_maze[next_cell.row][next_cell.col] |= 8;          // 1000 : Remove top wall
    }
    else if (row_diff == -1) {
        m_maze[current_cell.row][current_cell.col] |= 8;    // 1000 : Remove top wall
        m_maze[next_cell.row][next_cell.col] |= 2;          // 0010 : Remove bottom wall
    }
    else if (col_diff == 1) {
        m_maze[current_cell.row][current_cell.col] |= 4;    // 0100 : Remove right wall
        m_maze[next_cell.row][next_cell.col] |= 1;          // 0001 : Remove left wall
    }
    else if (col_diff == -1) {
        m_maze[current_cell.row][current_cell.col] |= 1;    // 0001 : Remove left wall
        m_maze[next_cell.row][next_cell.col] |= 4;          // 0100 : Remove right wall
    }
}
