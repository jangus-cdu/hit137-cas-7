import turtle

def draw_branch(t, branch_length, angle_left, angle_right, reduction_factor, depth):
    """
    Recursively draws a tree pattern.

    Parameters:
    - t: turtle object
    - branch_length: current branch length
    - angle_left: left branch angle
    - angle_right: right branch angle
    - reduction_factor: factor to reduce branch length
    - depth: remaining recursion depth
    """
    if depth == 0:
        return

    # Draw the current branch
    t.forward(branch_length)

    # Draw the left subtree
    t.left(angle_left)
    draw_branch(t, branch_length * reduction_factor, angle_left, angle_right, reduction_factor, depth - 1)
    t.right(angle_left)  # Return to the main branch

    # Draw the right subtree
    t.right(angle_right)
    draw_branch(t, branch_length * reduction_factor, angle_left, angle_right, reduction_factor, depth - 1)
    t.left(angle_right)  # Return to the main branch

    # Go back to the starting point of this branch
    t.backward(branch_length)

def Assignment_N2_Q3_tree_pattern():
    try:
        # Get user input
        print("Please enter the parameters for the tree pattern:")
        angle_left = float(input("Enter the left branch angle (degrees): "))
        angle_right = float(input("Enter the right branch angle (degrees): "))
        branch_length = float(input("Enter the starting branch length (pixels): "))
        depth = int(input("Enter the recursion depth: "))
        reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7 for 70%): "))

        if not (0 < reduction_factor < 1):
            raise ValueError("Reduction factor must be between 0 and 1 (exclusive).")
        if depth <= 0:
            raise ValueError("Recursion depth must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        print("Please restart the script and enter valid values.")
        return

    # Set up the turtle screen and object
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Recursive Tree Pattern")

    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)  # Point the turtle upwards
    t.penup()
    t.goto(0, -int(screen.window_height() / 2) + 50)  # Start at the bottom of the screen
    t.pendown()

    print("Drawing the tree...")

    # Draw the tree
    draw_branch(t, branch_length, angle_left, angle_right, reduction_factor, depth)
    print("Tree drawing complete. Close the turtle graphics window to exit.")

    # Wait for user to close the window
    screen.mainloop()

if __name__ == "__main__":
    Assignment_N2_Q3_tree_pattern()
