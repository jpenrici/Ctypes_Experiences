#pragma once


class Point {

    double m_x = 0;
    double m_y = 0;

public:
    Point() = default;
    Point(double x, double y) : m_x(x), m_y(y) {}

    Point(const Point &) = delete;
    Point(Point &&) = delete;
    ~Point() = default;

    auto operator=(const Point &) -> Point & = delete;
    auto operator=(Point &&) -> Point & = delete;

    auto X() const -> double;
    void X(double value);

    auto Y() const -> double;
    void Y(double value);
};

extern "C" {

Point * create(double x, double y);
auto getX(Point * obj) -> double;
void setX(Point * obj, double x);
auto getY(Point * obj) -> double;
void setY(Point * obj, double y);
void destroy(Point * obj);

}
