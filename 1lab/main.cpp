//#include <iostream>
//
//using namespace std;
//
//int main() {
////    freopen("input.txt","r",stdin);
////    freopen("output.txt","w",stdout);
//    int a[20][20], n;
//    cin >> n;
//    for(int i = 0; i < n; i++){
//        for(int j= 0; j < n; j++){
//            cin >> a[i][j];
//        }
//    }
//
//
//    for(int i = 0; i < n; i++){
//        for(int j = 0; j < n; j++){
//            cout << a[i][j] << "\t";;
//        }
//        cout << endl;
//    }
//    return 0;
//}
#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

//4
//1 4 2 6 7
//1 6 3 6 7
//3 4 6 3 6
//3 9 6 5 4
int main() {
    freopen("input.txt", "r", stdin);
    int n;
    cin >> n;

    float det = 1;
    double a[n][n + 1];
    double b[n][n + 1];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= n; j++) {
            cin >> a[i][j];
            b[i][j] = a[i][j];
        }
    }
    double x[n];
    double r[n];
    int i, j, k;
    int q = 0, w = 0;
    // прямой ход метода Гаусса с выбором главного элемента по столбцу
    for (i = 0; i < n; i++) {
        int max_row = i;
        double max_val = abs(a[i][i]);

        // поиск максимального элемента в текущем столбце
        for (j = i + 1; j < n; j++) {
            double val = abs(a[j][i]);
            if (val > max_val) {
                max_val = val;
                max_row = j;
            }
        }

        // обмен строк, если максимальный элемент не находится на текущ
        if (max_row != i) {
            for (k = i; k <= n; k++) {
                swap(a[i][k], a[max_row][k]);
            }
        }
        w++;
        if (w <= 2) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j <= n; j++) {
                    if (q >= 1 && i >= 1 && j == 0) {
                        cout << 0 << "\t";
                    } else if (q >= 2 && i == 2 && j == 1) {
                        cout << 0 << "\t";
                    } else {
                        cout << a[i][j] << "\t";
                    }
                }
                cout << endl;
            }
            cout << endl;
        }

        // прямой ход метода Гаусса для текущей строки
        for (int j = i + 1; j < n; j++) {
            double coeff = a[j][i] / a[i][i];
            for (int k = i + 1; k <= n; k++) {
                a[j][k] -= coeff * a[i][k];
            }
        }
        q++;
        if (q <= 2) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j <= n; j++) {
                    if (q >= 1 && i >= 1 && j == 0) {
                        cout << 0 << "\t";
                    } else if (q >= 2 && i == 2 && j == 1) {
                        cout << 0 << "\t";
                    } else {
                        cout << a[i][j] << "\t";
                    }
                }
                cout << endl;
            }
            cout << endl;
        }
    }

    //вывод определителя
    for (int i = 0; i < n; i++) {
        det = det * a[i][i];
    }
    if (det == 0) {
        cout << "invalid input data";
        return 0;
    }
    cout << "det = " << det << endl;

    // вывод треугольной матрицы
    cout << "Triangular matrix:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= n; j++) {
            if (j >= i) {
                cout << a[i][j] << "\t";
            } else {
                cout << 0 << "\t";
            }
        }
        cout << endl;
    }
// обратный ход метода Гаусса
    for (i = n - 1; i >= 0; i--) {
        x[i] = a[i][n] / a[i][i];
        for (j = i - 1; j >= 0; j--) {
            a[j][n] = a[j][n] - a[j][i] * x[i];
        }
    }
// вывод решений системы уравнений
    cout << "solve: \n";
    for (i = 0; i < n; i++) {
        cout << "x[" << i << "] = " << x[i] << endl;
    }
    //вывод невязок
    cout << "residuals: \n";
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            b[i][n] = b[i][n] - x[j] * b[i][j];
        }
    }
    for (int i = 0; i < n; i++) {
        cout << "r[" << i << "] = " << b[i][n] << endl;
    }
    return 0;
}

