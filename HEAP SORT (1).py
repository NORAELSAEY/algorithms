#!/usr/bin/env python
# coding: utf-8

# In[1]:


def max_heapify(arr, n, i):
    """Ensure the subtree rooted at index i is a max-heap."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap and continue heapifying if the root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    """Build a max-heap from the input array."""
    n = len(arr)
    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heap_sort(arr):
    """Sort an array using the Heap-Sort algorithm."""
    n = len(arr)
    # Step 1: Build a max-heap
    build_max_heap(arr)

    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Swap the root (max element) with the last element
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify the reduced heap
        max_heapify(arr, i, 0)

# Example Usage
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    print("Original Array:", arr)
    heap_sort(arr)
    print("Sorted Array:", arr)

