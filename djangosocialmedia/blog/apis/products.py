from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from djangosocialmedia.api.pagination import LimitOffsetPagination
from djangosocialmedia.blog.models import Product

from djangosocialmedia.blog.apis.services.products import create_product
from djangosocialmedia.blog.apis.selectors.products import get_products
from drf_spectacular.utils import extend_schema

class ProductApi(APIView):

    class Paggination(LimitOffsetPagination):
        default_limit = 15

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ('name', 'created_at', 'updated_at')

    @extend_schema(request=InputSerializer, responses=OutputSerializer)
    def post(self ,request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try :
            query = create_product(name=serializer.validated_data.get("name"))

        except Exception as ex:
            return Response(
                f'database Error {ex}',
                status.HTTP_400_BAD_REQUEST
            )
        return Response(self.OutputSerializer(query, context={"request":request}).data)
    
    @extend_schema(responses=OutputSerializer)
    def get(self, request):
        query = get_products()
        return Response(self.OutputSerializer(query, context={'request':request}, many=True).data)


 

