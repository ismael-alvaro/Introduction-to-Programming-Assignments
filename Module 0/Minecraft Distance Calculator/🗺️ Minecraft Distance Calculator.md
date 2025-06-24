# 🗺️ Minecraft Distance Calculator

## 🎯 Problem Statement

This problem involves calculating the Euclidean distance between two points in a 2D coordinate system, specifically within the context of a Minecraft-like environment. In Minecraft, the world is composed of cubic blocks, where each edge measures 1 meter. Locations are typically identified by (X, Y, Z) coordinates, representing longitude, elevation, and latitude, respectively. For surface-level communication, locations are often simplified to (X, Z) coordinates, abstracting the Y (elevation) component.

The task is to determine the 2D Euclidean distance from a given current location (X, Z) to three predefined village locations:

- **Hogsmeade**: (X: 34, Z: 220)
- **Kakariko**: (X: 0, Z: 0)
- **Solitude**: (X: 140, Z: 456)

The Euclidean distance formula in 2D is given by:

$D = \sqrt{(X_1 - X_2)^2 + (Z_1 - Z_2)^2}$

### 📥 Input Specification

The program expects two lines of integer input:

- `X`: An integer representing the current X-coordinate.
- `Z`: An integer representing the current Z-coordinate.

**Note**: The input will always be in the described format.

### 📤 Output Specification

The program should produce three lines of output, each displaying the calculated distance to a specific village, formatted to two decimal places:

- `Distancia para Hogsmeade: H`
- `Distancia para Kakariko: K`
- `Distancia para Solitude: S`

Where `H`, `K`, and `S` are floating-point numbers representing the distances.

### 💡 Examples

To illustrate the expected behavior, consider the following test cases:

| Case | Input (X) | Input (Z) | Output (Hogsmeade) | Output (Kakariko) | Output (Solitude) |
| :--- | :-------- | :-------- | :----------------- | :---------------- | :---------------- |
| 1    | 15        | 39        | 181.99             | 41.79             | 435.33            |
| 2    | 10        | 10        | 211.37             | 14.14             | 464.56            |
| 3    | 56        | 110       | 112.18             | 123.43            | 356.05            |

## 🧠 Solution Approach

My solution calculates the 2D Euclidean distance from a given point to three fixed points. It involves reading the current X and Z coordinates, applying the distance formula for each village, and formatting the output to two decimal places.

1.  **Input Reading**: The program first reads the current X and Z coordinates from the standard input.
2.  **Distance Calculation**: For each village, the Euclidean distance is calculated using the formula $D = \sqrt{(X_1 - X_2)^2 + (Z_1 - Z_2)^2}$. Python's `math.sqrt()` function is used for the square root, and the `** 2` operator for squaring.
3.  **Output Formatting**: The calculated distances, which are floating-point numbers, are then formatted to exactly two decimal places using f-strings or the `format()` method, as required by the problem statement.

This approach ensures accurate distance calculations and adherence to the specified output format.

## 💻 Code Implementation

```python
import math

X = int(input())
Z = int(input())

H = "{:,.2f}".format(math.sqrt((X - 34) ** 2 + (Z - 220) ** 2))
K = "{:,.2f}".format(math.sqrt((X - 0) ** 2 + (Z - 0) ** 2))
S = "{:,.2f}".format(math.sqrt((X - 140) ** 2 + (Z - 456) ** 2))

print("Distancia para Hogsmeade: " + str(H))
print("Distancia para Kakariko: " + str(K))
print("Distancia para Solitude: " + str(S))
```

