...
 Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5
...
input_data = input("Enter elements separated by spaces: ")
set_data = set(map(int, input_data.split()))
print(" ".join(map(str, set_data)))
