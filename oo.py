import pandas as pd
import numpy as np


def fl_ser():
    n = np.arange(41, 60, 2.5)
    s = pd.Series(n)
    print(s)


fl_ser()
sampleArray = np.array([[3, 6, 9, 12], [15, 18, 21, 24],
                        [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])

print("Printing Input Array")
print(sampleArray)

print("\n Printing array of odd rows and even columns")
newArray = sampleArray[::2, 1::2]
print(newArray)


def fl_scv():
    print(pd.Series(44, range(1, 11)))


fl_scv()


def pro3():  # Creating series from a dictionary

    d = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30}
    s = pd.Series(d)
    print("Series from dictionary")
    print(s)  # Creating series from an ndarray
    ar = np.array([2, 3, 4, 5, 6])
    print("\nSeries from ndarray")
    s1 = pd.Series(ar)
    print(s1)


pro3()


# def Ser_stumarks():
#     std_marks = []
#     for i in range(1, 6):
#         m = int(input("Enter the Percentile:"))
#         std_marks.append(m)
#     s = pd.Series(index=range(1201, 1206), data=std_marks)
#     print("Data fetched from the series are:")
#     print(s[s >= 75])


# Ser_stumarks()


# def Ser_stumarks():
#     std_marks = []
#     for i in range(1, 11):
#         m = int(input("Enter the marks:"))
#         std_marks.append(m)
#     s = pd.Series(index=range(1201, 1211), data=std_marks)
#     s[s < 33] = s+5
#     print("New List is:")
#     print(s[s >= 33])


# Ser_stumarks()
list = [33, 55, 65, 29, 19, 23]
ser = pd.Series(list)
val_sum = 0
sum5 = sum(ser[ser % 10 == 5])
sum3 = sum(ser[ser % 10 == 3])
print(sum3+sum5)


numbers = []
# Generating a series
for i in range(1, 11):
    val = int(input("Enter a number :"))
    numbers.append(val)
    ser = pd.Series(numbers)
    # Changing the values of multiple of four and assigning them a value
21
ser[ser % 4 == 0] = 21
print(ser)
