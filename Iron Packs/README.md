# 📊 Fair Share Distribution Algorithm

## 🎯 Problem Statement

This problem addresses a common scenario in resource management: distributing a total quantity of items equally among a fixed number of recipients, while accounting for any indivisible remainder. The objective is to determine the exact quantity each recipient receives and the total quantity that cannot be distributed and must be set aside or discarded.

### 📥 Input Specification

The program expects a single line of input:

- `P`: A natural number representing the total quantity of items available for distribution. The value of `P` will always be `3` or greater (`3 <= P`).

### 📤 Output Specification

The program should produce two lines of output:

1.  `V`: A natural number indicating the quantity of items distributed to each recipient.
2.  `F`: A natural number representing the quantity of items that remain undistributed.

### 💡 Examples

To illustrate the expected behavior, consider the following test cases:

| Case | Input (P) | Output (V) | Output (F) |
| :--- | :-------- | :--------- | :--------- |
| 1    | 20        | 6          | 2          |
| 2    | 3         | 1          | 0          |
| 3    | 10        | 3          | 1          |

## 🧠 Solution Approach

My solution to the "Fair Share Distribution" problem utilizes fundamental arithmetic operations in Python to efficiently calculate the distributed quantity and the remainder. The core logic relies on integer division and basic subtraction.

1.  **Integer Division for Equal Distribution**: To determine the quantity each of the three recipients receives, I perform an integer division of the total items (`P`) by the number of recipients (3). This operation automatically truncates any fractional part, yielding the whole number of items each recipient gets.

    ```python
    V = P // 3  # Using integer division for clarity
    ```

2.  **Calculating the Remainder**: The quantity of items that remain undistributed (`F`) is simply the total items minus the total items successfully distributed to all recipients. This is calculated by multiplying the items per recipient (`V`) by the number of recipients (3) and subtracting this product from the initial total (`P`).

    ```python
    F = P - (V * 3)
    ```

This approach ensures an accurate and fair distribution, correctly identifying any surplus items that cannot be evenly divided.

## 💻 Code Implementation

```python
P = int(input())
V = int(P/3)
F = P - (V * 3)
print(V)
print(F)
```

