class Program:

    def __init__(self, program):
        self.program = program
        self.sub_programs = []
        self.pc_list = []
    
    def set_program(self, program):
        self.program = program
    
    def get_program(self):
        return self.program
    
    def set_sub_programs(self, sub_programs):
        self.sub_programs = sub_programs
    
    def get_sub_programs(self):
        return self.sub_programs

    def set_pc_list(self, pc_list):
        self.pc_list = pc_list
    
    def get_pc_list(self):
        return self.pc_list
    
    def add_pc(self, product_code):
        self.pc_list.append(product_code)
    
    def remove_pc(self, product_code):
        self.pc_list.remove(product_code)
    
    def add_sub_program(self, sub_program):
        self.sub_programs.append(sub_program)
    
    def remove_sub_program(self, sub_program):
        self.sub_programs.remove(sub_program)