from PIL import Image, ImageDraw

def text_To_Image(content):
    img = Image.new('RGB', (100, 30), color = (73, 109, 137))
 
    d = ImageDraw.Draw(img)
    d.text((10,10), content, fill=(255,255,0))
 
    return img

import uuid
import os

def get_file_path_1(instance, filename):
    filename = instance.year + "_" + instance.month + "_" + instance.content_grade + "_" + instance.category + "_" + instance.content_number_begin + "_" + instance.content_number_end + ".pdf"
    return os.path.join('uploads/images/content_1', filename)

def get_file_path_2(instance, filename):
    filename = object_name = instance.publisher + "_" + instance.author + "_" + instance.content_label + "_" + instance.content_chapter + "_" + instance.category + "_" +  instance.content_number_begin + "_" + instance.content_number_end + ".pdf"
    return os.path.join('uploads/images/content_2', filename)

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def file_division(original_path, file_name, file_index, new_path):
    item_path = os.path.join(original_path, file_name + ".pdf")
    
    pdf = PdfFileReader(open(item_path, 'rb'))

    numberPages = pdf.getNumPages()

    for page in range(0, numberPages):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_name = file_name+ "_" + file_index[page]+".pdf"
        save_path = os.path.join(new_path, output_name)

        with open(save_path, 'wb') as f:
            pdf_writer.write(f)

def file_mix(original_path, original_file_prefix, original_file_index_list, new_file_path):

    pdf_writer = PdfFileWriter()
    output_name = original_file_prefix

    for i in original_file_index_list:
        original_file_name = original_file_prefix + "_" + i +".pdf"
        item_path = os.path.join(original_path, original_file_name)

        pdf = PdfFileReader(open(item_path, 'rb'))
        pdf_writer.addPage(pdf.getPage(0))
        output_name = output_name + "_" + i

    output_name = output_name + ".pdf"
    save_path = os.path.join(new_file_path, output_name)

    with open(save_path, 'wb') as f:
        pdf_writer.write(f)
    
    return output_name