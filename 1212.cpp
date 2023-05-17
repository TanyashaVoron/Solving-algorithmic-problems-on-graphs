#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

int N, M, L, K;

struct point { int x, y; };

int add(point a, point b, bool reverse) // вычислениe количества кораблей между двумя точками
{
    int W = reverse ? N : M;
    if(reverse)
        std::swap(a.x, a.y), std::swap(b.x, b.y);
    if(a.y == b.y)
        return std::max(0, b.x-a.x-K);
    else
        return std::max(0, (b.y-a.y-1))*std::max(0, 1+W-K)
             + std::max(0, b.x-K) + std::max(1+W-a.x-K, 0);
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::vector<point> v, h; // для хранения запрещенных точек по горизонтали и вертикали.
    std::cin >> N >> M >> L;
    while(L--) // ввод координат запрещенных точек
    {
        int x, y, l;
        char c;
        std::cin >> x >> y >> l >> c;
        point lr, ul = { std::max(1, x-1), std::max(1, y-1) }; //объявление координат верхнего левого и нижнего правого углов корабля
        if(c == 'V') // проверка ориентации корабля (вертикальная или горизонтальная)
            lr = { std::min(x+1, M), std::min(y+l, N) };
        else
            lr = { std::min(x+l, M), std::min(y+1, N) };
        for(int x = ul.x; x <= lr.x; x++)  // цикл для заполнения векторов запрещенных точек вокруг и внутри корабля
            for(int y = ul.y; y <= lr.y; y++)
                v.push_back( { x, y } ), h.push_back( { x, y });

    }
    h.insert(h.end(), { { 0, 1 }, { M+1, N } }); // добавление двух точек, обозначающих границы поля, в вектор запрещенных точек по горизонтали/вертикали
    v.insert(v.end(), { { 1, 0 }, { M, N+1 } }); // вертикали
    std::cin >> K;
    std::sort(v.begin(), v.end(), [] (point& a, point& b)
                                      { return a.x == b.x ? a.y < b.y : a.x < b.x; }); // сортировка вектора запрещенных точек по горизонтали/вертикали
    std::sort(h.begin(), h.end(), [] (point& a, point& b)
                                     { return a.y == b.y ? a.x < b.x : a.y < b.y; } );
    int ans = 0;
    for(int i = 1; i < h.size(); i++)
        ans += add(h[i-1], h[i], false); // вычисление количества кораблей между соседними точками в векторе запрещенных точек по горизонтали/вертикали
    for(int i = 1; i < v.size(); i++)
        ans += add(v[i-1], v[i], true);
    std::cout << (K == 1 ? ans/2 : ans) << std::endl;
}

// Сложность алгоритма: O(L)