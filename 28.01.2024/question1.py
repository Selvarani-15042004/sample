#You will be given a list of integers, , and a single integer . You must create an array of length  from elements of  such that its unfairness is minimized. Call that array . Unfairness of an array is calculated as

#Where:
# max denotes the largest integer in 
#- min denotes the smallest integer in 

@Example



#Pick any two elements, say .

#Testing for all pairs, the solution  provides the minimum unfairness.

#Note: Integers in  may not be unique.

#Function Description

#Complete the maxMin function in the editor below.
#maxMin has the following parameter(s):

#int k: the number of elements to select
#int arr[n]:: an array of integers
#Returns

#int: the minimum possible unfairness
#Input Format

#The first line contains an integer , the number of elements in array .
#The second line contains an integer .
#Each of the next  lines contains an integer  where .

#Constraints




#Sample Input 0

#7
#3
#10
#100
#300
#200
#1000
#20
#30
#Sample Output 0

#20
#Explanation 0

#EHere ; selecting the  integers , unfairness equals

#Emax(10,20,30) - min(10,20,30) = 30 - 10 = 20
#ESample Input 1

#E10
#E4
1
2
3
4
10
20
30
40
100
200
Sample Output 1

3
Explanation 1

Here ; selecting the  integers , unfa

max(1,2,3,4) - min(1,2,3,4) = 4 - 1 = 3
Sample Input 2

5
2
#1
#2
#1
#2
#1
#Sample Output 2

#0
#Explanation 2



def maxMin(k, arr):
    # Sort the array in ascending order
    arr.sort()
    n=len(arr)
    xmin=arr[-1]        
    for i in range(n-k+1):
        
        if arr[i+k-1]-arr[i]<xmin:
            xmin=arr[i+k-1]-arr[i]
    return xmin
if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

