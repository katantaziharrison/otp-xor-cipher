"""
Integer and Byte-Array Conversion

This program demonstrates how to:
1. Convert an arbitrary-sized non-negative integer into a byte array
   of a specified size.
2. Convert the byte array back into the original integer.

The example uses little-endian byte order, meaning that the
least-significant byte is stored first.
"""
def integer_to_bytes(n: int, size: int) -> bytes:
    """
    Convert a non-negative integer to a byte array of a specified size.

    Args:
        n (int): The non-negative integer to convert.
        size (int): The desired size of the resulting byte array.

    Returns:
        bytes: A byte array representing the integer in little-endian order.

    Raises:
        ValueError: If the integer is negative or if it cannot fit in the specified size.
    """
    if n < 0:
        raise ValueError("Integer must be non-negative.")
    
    if size <= 0:
        raise ValueError("Size must be a positive integer.")
    
    try:
        return n.to_bytes(size, byteorder='little', signed=False)
    
    except OverflowError as error:
        raise ValueError(f"Integer {n} cannot fit in {size} bytes.") from error
    

def bytes_to_integer(byte_array: bytes) -> int:
    """Convert a byte array back into the original integer."""
    return int.from_bytes(byte_array, byteorder='little', signed=False)

if __name__ == "__main__":
    # Example usage
    original_integer = 12345678901234567890
    byte_array_size = 16  # Specify the size of the byte array
    
    # Convert integer to a fixed-size little-endian byte array
    byte_array = integer_to_bytes(original_integer, byte_array_size)
    print(f"Original Integer: {original_integer}")

    # Convert the byte array back to the original integer
    recovered_integer = bytes_to_integer(byte_array)
    print(f"Recovered Integer: {recovered_integer}")

    # Format the byte array as a hexadecimal string for display
    hexadecimal_representation = [f"{byte:02x}" for byte in byte_array]
    print(f"Byte Array (Hex): {hexadecimal_representation}") 

    if original_integer == recovered_integer:
        print("Success: The recovered integer matches the original integer.")
    else:
        print("Error: The recovered integer does not match the original integer.")   
    