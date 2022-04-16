import os
import io

from google.cloud import vision


def main():
    client = vision.ImageAnnotatorClient()
    file_name = os.path.abspath('18.png')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image_context = vision.ImageContext(language_hints=["ja"])
    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.text_detection(image=image, image_context=image_context)
    import pdb; pdb.set_trace()
    for i, block in enumerate(response.full_text_annotation.pages[0].blocks):
        block_text = ""
        for paragraph in block.paragraphs:
            for word in paragraph.words:
                block_text += "".join([symbol.text for symbol in word.symbols])
                latest_vertices = word.bounding_box.vertices[0]
        print(i, block_text, latest_vertices)

    full_text = response.full_text_annotation.text
    #print(full_text)



if __name__=="__main__":
    main()