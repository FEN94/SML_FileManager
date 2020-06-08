class ProductCode:

    def __init__(self, product_code, program, sub_program, printing_type):
        self.product_code = product_code
        self.program = program
        self.sub_program = sub_program
        self.printing_type = printing_type
        self.styles = 1
        self.image = False
    
    def set_product_code(self, product_code):
        self.product_code = product_code
    
    def get_product_code(self):
        return self.product_code
    
    def set_program(self, program):
        self.program = program
    
    def get_program(self):
        return self.program

    def set_sub_program(self, sub_program):
        self.sub_program = sub_program
    
    def get_sub_program(self):
        return self.sub_program
    
    def set_printing_type(self, printing_type):
        self.printing_type = printing_type
    
    def get_printing_type(self):
        return self.printing_type
    
    def set_styles(self, styles):
        self.styles = styles
    
    def get_styles(self):
        return self.styles
    
    def set_image(self, image):
        self.image = image
    
    def is_image(self):
        return self.image