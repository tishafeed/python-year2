import argparse

parser = argparse.ArgumentParser(description='А python script that solver a knapsack problem through recursion')
# the overall size of knapsack, if none specified, then 0
parser.add_argument('-W', help='capacity', type=float, default=0)

# a plus is there so there is at least one argument for weights, this produces a list of weights
parser.add_argument('-w', help='weights', nargs='+')

args = parser.parse_args()
maxsize = args.W
weights = list(map(int, args.w))


def sack(index, space_left):
    if index == 0:  # base case
        return weights[0]
    elif space_left == 0:  # end case
        return 0
    elif weights[index] > space_left:  # skip if current element doesn't fit
        return sack(index - 1, space_left)
    else:
        way1 = sack(index - 1, space_left)
        way2 = weights[index] + sack(index - 1, space_left - weights[index])
        return max(way1, way2)  # find the most optimal variant through recursion


print(sack(len(weights)-1, maxsize))  # print out the result
