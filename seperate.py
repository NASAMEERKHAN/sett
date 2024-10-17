...
Write a program to get n number of values in separate line for set and print the values with space separation.
Sample Input:
5
3
1
4
5
2
...
n = int(input("Enter the number of elements: "))
elements = set()

for _ in range(n):
    element = int(input())
    elements.add(element)

print(" ".join(map(str, elements)))
