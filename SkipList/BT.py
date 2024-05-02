class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if root.key == key:
        return root
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = get_min_value(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def get_min_value(root):
    while root.left is not None:
        root = root.left
    return root

def printTree(root, space):
        if root == None:
            return ""
        space += 5
        printTree(root.right, space)
        for i in range(5, space):
            print(end=" ")
        print(root.key)
        printTree(root.left, space)


print("TREE 1")
root = insert(None, 20)
printTree(root, 0)
print("TREE 2")
root = insert(root, 40)
printTree(root, 0)
print("TREE 2")
root = insert(root, 10)
printTree(root, 0)
print("TREE 3")
root = insert(root, 20)
printTree(root, 0)
print("TREE 4")
root = insert(root, 5)
printTree(root, 0)
print("TREE 5")
root = insert(root, 80)
printTree(root, 0)
print("TREE 6")
root = delete(root, 20)
printTree(root, 0)
print("TREE 7")
root = insert(root, 100)
printTree(root, 0)
print("TREE 8")
root = insert(root, 20)
printTree(root, 0)
print("TREE 9")
root = insert(root, 30)
printTree(root, 0)
print("TREE 10")
root = delete(root, 5)
printTree(root, 0)
print("TREE 11")
root = insert(root, 50)
printTree(root, 0)