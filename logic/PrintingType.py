class PrintingType:

    def __init__(self, printing_type):
        self.printing_type = printing_type
        self.programs = []
    
    def set_priting_type(self, printing_type):
        self.printing_type = printing_type
    
    def get_printing_type(self):
        return self.printing_type
    
    def set_programs(self, programs):
        self.programs = programs
    
    def get_programs(self):
        return self.programs
    
    def add_program(self, program):
        self.programs.append(program)
    
    def remove_program(self, program):
        self.programs.remove(program)