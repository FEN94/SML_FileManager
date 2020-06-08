import os
from zipfile import ZipFile
from shutil import copyfile, rmtree
from PyQt5.QtWidgets import QMessageBox
from subprocess import Popen

found_pc = False


def message(msg_type, msg):
    msg_window = QMessageBox()
    msg_window.setIcon(msg_type)
    msg_window.setText(msg)
    msg_window.setStandardButtons(QMessageBox.Ok)
    msg_window.show()
    msg_window.exec()


def search_pc(path, pc):  # Return Product Code path
    global found_pc
    file_list = os.listdir(path)
    for i in file_list:
        if pc in file_list:
            found_pc = True
            pc_path = path + "/" + pc
            return pc_path
        else:
            try:
                new_path = path+"/"+i
                p = search_pc(new_path, pc)
                if found_pc:
                    return p
            except NotADirectoryError:
                pass


def get_approval(app_path, pc):
    file_list = os.listdir(app_path)
    for approval in file_list:
        if approval[:len(pc)] == pc and approval[-3:] == "pdf":
            return approval


def make_zip(product_list, printing_type):
    global found_pc
    pc_list = product_list.keys()
    os.mkdir("C:/GMC/Approvals")
    for product_code in pc_list:
        found_pc = False
        path = search_pc("C:/GMC/"+printing_type, product_code) + "/WFD"
        if product_list[product_code] > 1:
            style_list = next(os.walk(path))[1]
            for style in style_list:
                path_wstyle = path + "/" + style
                if product_code + style + "_APP.pdf" in os.listdir(path_wstyle):
                    copyfile(path_wstyle+"/"+product_code+style+"_APP.pdf", "C:/GMC/Approvals/"+product_code+style+"_APP.pdf")
        else:
            if product_code + "001_APP.pdf" in os.listdir(path):
                copyfile(path + "/" + product_code + "001_APP.pdf", "C:/GMC/Approvals/" + product_code + "001_APP.pdf")
    zip_folder = ZipFile("C:/GMC/Approvals.zip", "w")
    approval_list = os.listdir("C:/GMC/Approvals")
    for i in approval_list:
        zip_folder.write("C:/GMC/Approvals/" + i)
    rmtree("C:/GMC/Approvals")


def make_folder(pc_list, nice_label):
    # [['product_code', printing_type, style_num, sub_program, logo]] for GMC
    # [['product_code', printing_type, style_num, sub_program]] for NiceLabel
    if nice_label:
        gmc_nl = "C:/NiceLabel/"
    else:
        gmc_nl = "C:/GMC/"
    for pc in pc_list:
        src_path = gmc_nl + pc[1]
        src_path += "/" + pc[0][:2]
        try:
            os.mkdir(src_path)
        except FileExistsError:
            pass
        if pc[3]:
            src_path += "/" + pc[0][2:4]
            try:
                os.mkdir(src_path)
            except FileExistsError:
                pass
        src_path += "/" + pc[0]
        rollback_folder = src_path
        try:
            os.mkdir(src_path)
            if nice_label is False:
                if pc[4]:
                    os.mkdir(src_path + "/LOGO")
                src_path += "/WFD"
                os.mkdir(src_path)
            if pc[2] > 1:
                make_styles_folder(src_path, pc[2])
            try:
                copyfile("C:/GMC/Checklist.xlsx", src_path + "/Checklist_" + pc[0] + ".xlsx")
                # message(QMessageBox.Information, "Folder(s) created successfully")
            except FileNotFoundError:
                message(QMessageBox.Critical, "Checklist not found in C:/GMC path")
                rmtree(rollback_folder)
                return False
        except FileExistsError:
            message(QMessageBox.Warning, pc[0] + " folder already exist")
            return False
    return True


def make_styles_folder(src_path, styles_num):
    for i in range(1, styles_num + 1):
        if len(str(i)) == 1:
            os.mkdir(src_path + "/00" + str(i))
        elif len(str(i)) == 2:
            os.mkdir(src_path + "/0" + str(i))
        elif len(str(i)) == 3:
            os.mkdir(src_path + "/" + str(i))


def gmc_product_code(product_code, printing_type):
    src_path = "C:/GMC/" + printing_type
    path = search_pc(src_path, product_code)
    if path != "" and path is not None:
        path += "/WFD"
        Popen('explorer ' + '"' + path.replace('/', '\\') + '"')
        global found_pc
        found_pc = False
    else:
        return False

def nicelabel_product_code(product_code):
    path = search_pc("C:/NiceLabel/Thermal", product_code)
    if path != "" and path is not None:
        Popen('explorer ' + '"' + path.replace('/', '\\') + '"')
        global found_pc
        found_pc = False
    else:
        return False

def open_product_code(gmc_or_nl, product_code, printing_type):
    if gmc_or_nl == 0:
        return gmc_product_code(product_code, printing_type)
    elif gmc_or_nl == 1:
        return nicelabel_product_code(product_code)

# make_zip({"US2900A": 2, "US2900B": 1}, "PFL")
# make_folder([["US2900A", "PFL", 2, True, False], ["US2900B", "PFL", 3, True, False]])
# copy_checklist(["US29HNW00C", "US29HNW00E", "US29M9W006", "US29M9W008"], "Offset")
# open_product_code("ONBAMKV001".strip())
# gmc_product_code("MKACMNV001".strip(), "PFL".strip())
