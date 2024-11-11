#დავალება N1

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def printLeafNodes(node):
    if node is not None:
        if node.left is None and node.right is None:
            print(node.value, end=" ")
        else:
            printLeafNodes(node.left)
            printLeafNodes(node.right)

def countEdges(node):
    if node is None:
        return 0
    left_edges = countEdges(node.left)
    right_edges = countEdges(node.right)
    return left_edges + right_edges + 1

# ბინარული ხის შექმნა
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Leaf nodes are:")
printLeafNodes(root)

print("\nNumber of edges:", countEdges(root) - 1)

#ეს კოდი წარმოადგენს ბინარულ ხეს Python-ში, სადაც თითოეულ კვანძს აქვს მაქსიმუმ ორი შვილი. 
# TreeNode კლასი აღწერს კვანძს. printLeafNodes ფუნქცია რექურსიულად გადის მთელ ხეზე და 
# ბეჭდავს მხოლოდ ფოთლოვან კვანძებს (რომლებსაც არ ჰყავთ შვილები). countEdges ფუნქცია კი 
# ითვლის კიდეების რაოდენობას. ბინარულ ხეში კიდეების რაოდენობა არის კვანძების რაოდენობა 
# მინუს 1, ამიტომ countEdges(root) - 1 გამოაქვეყნებს კიდეების რაოდენობას.
