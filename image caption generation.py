import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

# conditional image captioning
text = "a photography of"
inputs = processor(raw_image, text, return_tensors="pt")

out = model.generate(**inputs)
print(processor.decode(out[0], skip_special_tokens=True))

# unconditional image captioning
inputs = processor(raw_image, return_tensors="pt")

out = model.generate(**inputs)
print(processor.decode(out[0], skip_special_tokens=True))


'''
    1. Imports:

    requests: This library allows downloading images from URLs.
    PIL.Image: This library helps handle image loading and manipulation.
    transformers: This library provides pre-trained models for various Natural Language Processing (NLP) tasks, including the Blip model used in this code.
    BlipProcessor: This class is responsible for pre-processing both image and text data before feeding them to the Blip model.
    BlipForConditionalGeneration: This class is the actual Blip model specifically designed for conditional image captioning.
    2. Loading the Model and Processor:

    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large"):
    This line loads a pre-trained Blip processor from the "Salesforce/blip-image-captioning-large" model.
    The processor handles tasks like resizing images and converting text to a format suitable for the Blip model.
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large"):
    This line loads the actual Blip model for conditional image captioning from the same pre-trained source.
    3. Downloading and Preprocessing the Image:

    img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg':
    This line defines the URL of the image you want to generate captions for.
    raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB'):
    This part downloads the image from the URL:
    requests.get(img_url, stream=True) downloads the image data using the requests library. The stream=True argument ensures efficient downloading in chunks for large images.
    .raw accesses the raw image data stream.
    Image.open opens the raw data as a PIL Image object.
    .convert('RGB') converts the image to RGB format, which is often required by the Blip model for processing.
    4. Conditional Image Captioning:

    text = "a photography of":
    This line defines a starting phrase ("a photography of") that will guide the caption generation towards photography-related descriptions.
    inputs = processor(raw_image, text, return_tensors="pt"):
    This line combines the preprocessed image (raw_image) and the conditional text (text) using the Blip processor (processor).
    return_tensors="pt" specifies returning the processed data (image and text) as PyTorch tensors, which is the format the Blip model expects.
    5. Generating Caption with Conditional Text:

    out = model.generate(**inputs):
    This line feeds the combined image and text data (inputs) into the Blip model (model).
    The generate method of the model takes the input data and generates a caption based on both the image content and the provided text.
    The ** operator unpacks the inputs dictionary as separate arguments for the generate method.
    6. Decoding and Printing the Result:

    print(processor.decode(out[0], skip_special_tokens=True)):
    This line decodes the generated caption (out[0]). Remember, the model might generate captions with special tokens for internal processing.
    The Blip processor (processor) has a decode method that translates the model's output back into human-readable text.
    skip_special_tokens=True instructs the decoder to ignore any special tokens the model might have included in the caption.
    Finally, the decoded caption is printed.
    7. Unconditional Image Captioning (Optional):

    This part (commented out in some examples) removes the conditional text input. It's included for comparison.
    inputs = processor(raw_image, return_tensors="pt"):
    Here, only the preprocessed image (raw_image) is used as input, without any guiding text.
    The following steps (out = model.generate(**inputs), print(...)) are similar to the conditional case, but the generated caption will solely be based on the image content.
'''