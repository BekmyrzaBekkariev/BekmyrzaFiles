# C++
# 2 день 2022
# Задача F. МОНЕТЫ
# Сколькими способами можно заплатить данную цену 10-сомовыми,
# 5-сомовыми и 1-сомовыми монетами (перестановка монет не дает другого способа)?

# #include <iostream>
# using namespace std;

# int main()
# {
#     int n;
#     cin >> n;
#     int count = 0;
#     for (int i = 0; i <= n/10; i++) {
#         for (int j = 0; j <= n/5; j++) {
#             for (int k = 0; k <= n; k++) {
#                 if (10*i + 5*j + k == n) {
#                     count++;
#                 }
#             }
#         }
#     }
#     cout << count << endl;
#     return 0;
# }

# def count_ways(total_price, coin_types):
#     dp = [0] * (total_price + 1)
#     dp[0] = 1
#     for coin in coin_types:
#         for i in range(coin, total_price + 1):
#             dp[i] += dp[i - coin]
#     return dp[total_price]


# total_price = int(input())
# coin_types = [10, 5, 1]
# print(count_ways(total_price, coin_types))


# Задача G. МИНИМУМ
# А и B – заданные натуральные числа. X и Y – целые числа.
# Найти наименьшее возможное значение выражения
# (20*X+Y+A)2+(X+21*Y+B)2

# #include <iostream>
# #include <cmath>
# using namespace std;

# int main()
# {
#     int A, B;
#     cin >> A >> B;
#     int min_val = 2147483647;
#     for (int X = -100; X <= 100; X++) {
#         for (int Y = -100; Y <= 100; Y++) {
#             int val = (20*X + Y + A)*(20*X + Y + A) + (X + 21*Y + B)*(X + 21*Y + B);
#             min_val = min(min_val, val);
#         }
#     }
#     cout << min_val << endl;
#     return 0;
# }

# Задача H. ТЫНЫСТАНОВ
# Используются следующие латинские буквы: А (а), E (э,е), I (и), O (о), о (ө), U (у), u
# (ү), Y (ы). После каждой буквы может быть такая же буква или: после А – Y, после E – I,
# после I – E, после O – U, после о – u, после U – A, после u – o, после Y – A.
# Все такие слова, состоящие из пяти латинских букв, расположены в
# лексикографическом (словарном)порядке. По данному слову (не последнему слову
# YYYYY), найти следующее слово.

# #include <iostream>
# #include <string>
# using namespace std;

# string next_word(string word) {
#     int n = word.size();
#     for (int i = n-1; i >= 0; i--) {
#         if (word[i] == 'A') {
#             word[i] = 'Y';
#             return word;
#         }
#         else if (word[i] == 'E') {
#             word[i] = 'I';
#             return word;
#         }
#         else if (word[i] == 'I') {
#             word[i] = 'E';
#             return word;
#         }
#         else if (word[i] == 'O') {
#             word[i] = 'U';
#             return word;
#         }
#         else if (word[i] == 'o') {
#             word[i] = 'u';
#             return word;
#         }
#         else if (word[i] == 'U') {
#             word[i] = 'A';
#             return word;
#         }
#         else if (word[i] == 'u') {
#             word[i] = 'o';
#             return word;
#         }
#         else if (word[i] == 'Y') {
#             word[i] = 'A';
#         }
#     }
#     return word;
# }

# int main()
# {
#     string word;
#     cin >> word;
#     cout << next_word(word) << endl;
#     return 0;
# }

# Python
# def next_word(word):
#     n = len(word)
#     for i in range(n-1, -1, -1):
#         if word[i] == 'A':
#             word = word[:i] + 'Y' + word[i+1:]
#             return word
#         elif word[i] == 'E':
#             word = word[:i] + 'I' + word[i+1:]
#             return word
#         elif word[i] == 'I':
#             word = word[:i] + 'E' + word[i+1:]
#             return word
#         elif word[i] == 'O':
#             word = word[:i] + 'U' + word[i+1:]
#             return word
#         elif word[i] == 'o':
#             word = word[:i] + 'u' + word[i+1:]
#             return word
#         elif word[i] == 'U':
#             word = word[:i] + 'A' + word[i+1:]
#             return word
#         elif word[i] == 'u':
#             word = word[:i] + 'o' + word[i+1:]
#             return word
#         elif word[i] == 'Y':
#             word = word[:i] + 'A' + word[i+1:]
#     return word


# word = input()
# print(next_word(word))


# 4
# 123 324 315 999
# 9 729
# n = int(input())
# m = input().split()
# q = 0
# c = 0
# b = 0
# for i in range(0, n):
#     q = int(m[i])
#     if q % 2 == 0:
#         xc = 0
#         while q > 0:
#             xc += q % 10
#             q = q // 10
#         if c < xc:
#             c = xc
#     else:
#         xc = 1
#         while q > 0:
#             xc *= q % 10
#             q = q // 10
#         if b < xc:
#             b = xc
# print(c, b)
