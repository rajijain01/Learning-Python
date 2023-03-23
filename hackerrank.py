# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring



#example1:
#if __name__ == '__main__':
x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

print(coordinates)

#example2:question:rp9631831@gmail.com
#Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given
#scores. Store them in a list and find the score of the runner-up
#Input Format

#The first line contains
#The second line contains an array of integers each separated by a space
# take input from the user
n = int(input()) # number of scores
scores = list(map(int, input().split())) # list of scores

# remove duplicates and sort the list in descending order
scores = sorted(list(set(scores)), reverse=True)

# print the second highest score
print(scores[1])
