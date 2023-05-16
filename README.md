# BST-with-Python
implementation BST algorithm with python.
#### As you may know the BST algorithm is used for searching an element inside the a data. This algorithm gets a list of data and an element and determines that if that element exists in that list or not.
#### In this code we defined a Variable named LEN_OF_LIST which determines the length of the list and the NUM variable shows the number or an element we want to find in the given list.
 First of all let me describe the BST algorithm briefly:
#### We consider that the given list is sorted and it has n elements. The first step is to check the number we want to find with the middle element if it they are equals so we hit the target and we return true if it’s not equal we have to check either its higher or lower. If its lower we will find out our target is in the first half (lower half) so we just call the function recursively until we hit the target and if its higher we will do the same for the second part (higher). If we couldn’t find so we will return False.
