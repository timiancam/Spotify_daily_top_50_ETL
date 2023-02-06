from pptx import Presentation

def delete_shape(slide, idx):
    slide.shapes.element.remove(slide.shapes[idx].element)
