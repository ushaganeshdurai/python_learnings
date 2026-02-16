class PaintWork: 
    brand_count = 0  # Class variable
    
    def __init__(self, brand):
        self.brand = brand
        PaintWork.brand_count += 1
    
    # Static method - no self, no cls
    @staticmethod
    def required_items(items):  # Remove 'self'
        return [item.strip() for item in items.split(",")]
    
    # Class method - receives cls (the class itself)
    @classmethod
    def get_brand_count(cls):
        return f"Total brands: {cls.brand_count}"
    
    # Instance method - requires instantiation
    def sample(self):
        return f"{self.brand} used"

# Instance method - needs object
pw = PaintWork("AsianPaints")
print(pw.sample())  # Output: AsianPaints used

# Static method - can call on class or instance
inp = "brush, paint, roller"
print(PaintWork.required_items(inp))  # Output: ['brush', 'paint', 'roller']
print(pw.required_items(inp))         # Also works

# Class method - can call on class or instance
pw2 = PaintWork("Berger")
print(PaintWork.get_brand_count())  # Output: Total brands: 2
