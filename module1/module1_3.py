def show_value_and_type(value):
    """Display a value and its data type."""
    print("Value:", value)
    print("Data type:", type(value).__name__)


# Examples
show_value_and_type("Hello")
show_value_and_type(25)
show_value_and_type([1, 2, 3])
