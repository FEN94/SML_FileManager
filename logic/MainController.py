import os
# from zipfile import ZipFile
# from shutil import copyfile, rmtree
# from PyQt5.QtWidgets import QMessageBox
# from subprocess import Popen
from logic.PrintingType import PrintingType
from logic.Program import Program


class MainController():

    def __init__(self):
        self.found_pc = False
    
    def look_4programs(self, obj_printing_type):
        programs_list = next(os.walk('C:/' + obj_printing_type.get_printing_type()))
        # add Program to Printing Type program list
        for i in programs_list:
            program = Program(i)
            obj_printing_type.add_program(program)
    
    def look_4subp(self, obj_program):
        pass

    def setup(self):
        if 'sml_filemanager' not in next(os.walk('C:/'))[1]:
            os.mkdir('C:/sml_filemanager')
        try:
            file = open('C:/sml_filemanager/data.txt', 'rt')
        except FileNotFoundError:
            # Create PrintingType objects
            printing_types = ['Arc_Thermal', 'Digital', 'Offset', 'PFL', 'Woven']
            obj_printing_types = []
            for i in range(0, len(printing_types)-1):
                obj_printing_types[i] = PrintingType(obj_printing_types[i])
            # Loop through all printing type folders
            # for i in obj_printing_types:
            #     programs_list = next(os.walk('C:/' + i.get_printing_type()))[1]
            #     for j in programs_list:
            #         program = Program(j)
            #         i.add_program(program)
            open('C:/sml_filemanager/data.txt', 'xt')

    # def search_pc(self, path, pc):
    #     file_list = os.listdir(path)
    #     for i in file_list:
    #         if pc in file_list:
    #             self.found_pc = True
    #             pc_path = path + "/" + pc
    #             return pc_path
    #         else:
    #             try:
    #                 new_path = path + "/" + i
    #                 p = self.search_pc(new_path, pc)
    #                 if self.found_pc is True:
    #                     return p
    #             except NotADirectoryError:
    #                 pass

    # def get_approval(self, app_path, pc):
    #     file_list = os.listdir(app_path)
    #     for approval in file_list:
    #         if approval[:len(pc)] == pc and approval[-3:] == "pdf":
    #             return approval

    # def make_zip(self, productCode_list, printing_type):
    #     pc_list = productCode_list.keys()
    #     dst_path = "Approvals/"
    #     src_path = "C:/GMC/" + printing_type + "/"
    #     os.mkdir("Approvals")
    #     for pc in pc_list:
    #         pc_path = self.search_pc(src_path, pc)
    #         self.found_pc = False
    #         approval = self.get_approval(pc_path + "/WFD/", pc)
    #         app_path = pc_path + "/WFD/" + approval
    #         copyfile(app_path, dst_path + approval)
    #     zip_folder = ZipFile("Approvals.zip", "w")
    #     approval_list = os.listdir("Approvals/")
    #     for i in approval_list:
    #         zip_folder.write("Approvals/" + i)
    #     rmtree("Approvals")

    # def make_folder(self, pc_list):
    #     # [['MKAC001', printing_type, style_num, sub_program, logo]]
    #     for pc in pc_list:
    #         src_path = "C:/GMC/" + pc[1]
    #         src_path += "/" + pc[0][:2]
    #         try:
    #             os.mkdir(src_path)
    #         except FileExistsError:
    #             pass
    #         if pc[3]:
    #             src_path += "/" + pc[0][2:4]
    #             try:
    #                 os.mkdir(src_path)
    #             except FileExistsError:
    #                 pass
    #         src_path += "/" + pc[0]
    #         rollback_folder = src_path
    #         try:
    #             os.mkdir(src_path)
    #             if pc[4]:
    #                 os.mkdir(src_path + "/LOGO")
    #             src_path += "/WFD"
    #             os.mkdir(src_path)
    #             if pc[2] > 1:
    #                 self.make_styles_folder(src_path, pc[2])
    #             try:
    #                 copyfile("C:/GMC/Checklist.xlsx", src_path + "/Checklist_" + pc[0] + ".xlsx")
    #                 # message(QMessageBox.Information, "Folder(s) created successfully")
    #             except FileNotFoundError:
    #                 self.message(QMessageBox.Critical, "Checklist not found in C:/GMC path")
    #                 rmtree(rollback_folder)
    #                 return False
    #         except FileExistsError:
    #             self.message(QMessageBox.Warning, pc[0] + " folder already exist")
    #     return True

    # def make_styles_folder(self, src_path, styles_num):
    #     for i in range(1, styles_num + 1):
    #         if len(str(i)) == 1:
    #             os.mkdir(src_path + "/00" + str(i))
    #         elif len(str(i)) == 2:
    #             os.mkdir(src_path + "0" + str(i))
    #         elif len(str(i)) == 3:
    #             os.mkdir(src_path + str(i))

    # def open_product_code(self, product_code):
    #     srcs_list = ["C:/GMC/ARC_Thermal", "C:/GMC/Digital", "C:/GMC/Offset",
    #                  "C:/GMC/PFL", "C:/GMC/Woven"]
    #     path = ""
    #     for src_path in srcs_list:
    #         path = self.search_pc(src_path, product_code)
    #         if path != "" and path is not None:
    #             path += "/WFD"
    #             Popen('explorer ' + '"' + path.replace('/', '\\') + '"')
    #             self.found_pc = False
    #             break
    #     if path == "" or path is None:
    #         self.message(QMessageBox.Critical, "Product Code not found")