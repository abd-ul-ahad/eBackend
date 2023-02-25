# from django.shortcuts import render
# from django.http import JsonResponse
# import json
# from django.forms.models import model_to_dict
from Products.models import Products
from Products.serializers import ProductsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# imports for tensorflow
from tensorflow.keras.applications.resnet50 import  preprocess_input
import numpy as np
from tensorflow.keras.preprocessing import image
from keras.models import load_model
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


# imports for image to array

model = load_model(env('SEARCH_BY_IMAGE_PATH'))


@api_view(['GET'])
def Get_Products(request, *args, **kwargs):
    """http://127.0.0.1:8000/api/search/"""
    model_data = Products.objects.all()
    # @property method in Products.models
    sales_price = Products.objects.all().first().sales_price

    data = {}
    if model_data:
        # many=False if you want only one result
        data = ProductsSerializer(model_data, many=True).data

    return Response(data)


@api_view(['POST'])
def Post_Products(request, *args, **kwargs):
    """http://127.0.0.1:8000/api/search/post

    [The api is]
    {
        "product_name": "Product Name 2",
        "product_description": "Product description will show here",
        "product_color": "Blue",
        "product_available": true,
        "product_discount": "10%",
        "product_added_date": "2023-02-16T16:27:50.560000Z"
    }
    """
    data = {}

    try:
        # creating a array from image
        img = image.load_img("searchByImage/"+request.FILES["product_search_image"].name,
                             target_size=(224, 224))
        image_array = image.img_to_array(img)
        expand_img_array = np.expand_dims(image_array, axis=0)

        processed_image = preprocess_input(expand_img_array)

        result = model.predict(processed_image).flatten()

        product_unique_array = result/np.linalg.norm(result)

        return Response(product_unique_array)

    except Exception as e:
        print("Error! ", e)

    serializer = ProductsSerializer(data=request.data)

    data = {}
    if serializer.is_valid():
        instance = serializer.save()  # saves the data into database
        data = serializer.data
        print(instance)

    return Response(data)


# def api_home(request, *args, **kwargs):
#     body = request.body
#     data = {}

#     try:
#         data = json.loads(body)
#         data['headers'] = dict(request.headers)
#         data['content_type'] = request.content_type
#         # url query parameters ?abc=10 return {'abc': '10'}
#         data['params'] = dict(request.GET)
#     except Exception as e:
#         return JsonResponse({"message":  "Error"})

#     print(data['content_type'])
#     return JsonResponse({"Name":  "Abdul Ahad"})
