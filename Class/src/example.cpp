#include "../include/example.hpp"

#include <memory>


auto Point::X() const -> double
{
    return m_x;
}

void Point::X(double value)
{
    m_x = value;
}

auto Point::Y() const -> double
{
    return m_y;
}

void Point::Y(double value)
{
    m_y = value;
}

// Extern C
auto create(double x, double y) ->  Point *
{
    return new Point(x, y);
}

auto getX(Point *obj) -> double
{
    return obj->X();
}

void setX(Point *obj, double x)
{
    obj->X(x);
}

auto getY(Point *obj) -> double
{
    return obj->Y();
}

void setY(Point *obj, double y)
{
    obj->Y(y);
}

void destroy(Point *obj)
{
    delete obj;
}
