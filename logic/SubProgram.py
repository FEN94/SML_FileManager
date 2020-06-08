class SubProgram:

    def __init__(self, sub_program):
        self.sub_program = sub_program
        self.pc_list = []
    
    def set_sub_program(self, sub_program):
        self.sub_program = sub_program
    
    def get_sub_program(self):
        return self.sub_program
    
    def set_pc_list(self, pc_list):
        self.pc_list = pc_list
    
    def get_pc_list(self):
        return self.pc_list
    
    def add_pc(self, product_code):
        self.pc_list.append(product_code)
    
    def remove_pc(self, product_code):
        self.pc_list.remove(product_code)