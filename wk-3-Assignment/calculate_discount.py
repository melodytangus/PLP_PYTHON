def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
    
    Returns:
        float: The final price after discount (if discount >= 20%) or original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


def main():
    """Main function to interact with the user and calculate discounts."""
    print("=== Discount Calculator ===")
    
    try:
        # Get user input
        price = float(input("Enter the original price of the item: $"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Validate inputs
        if price < 0:
            print("Error: Price cannot be negative.")
            return
        
        if discount_percent < 0:
            print("Error: Discount percentage cannot be negative.")
            return
        
        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)
        
        # Display results
        print(f"\nOriginal price: ${price:.2f}")
        print(f"Discount percentage: {discount_percent}%")
        
        if discount_percent >= 20:
            discount_amount = price - final_price
            print(f"Discount applied: ${discount_amount:.2f}")
            print(f"Final price after discount: ${final_price:.2f}")
        else:
            print("No discount applied (discount must be 20% or higher)")
            print(f"Final price: ${final_price:.2f}")
            
    except ValueError:
        print("Error: Please enter valid numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()