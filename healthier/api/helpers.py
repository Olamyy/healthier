from rest_framework.response import Response
from rest_framework.views import APIView


class AbstractDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, id):
        self.ID = {self.ID_NAME: id}
        print(self.ID)
        try:
            return self.MODEL.objects.get(**self.ID)
        except self.MODEL.DoesNotExist:
            raise Http404
    
    def get_all(self):
        return self.MODEL.objects.all()

    def get(self, request, format=None):
        id = request.query_params.get(self.ID_NAME, None)
        if id:
            matching_object = self.get_object(id)
            serializer = self.SERIALIZER(matching_object)
            return Response(serializer.data)
        else:
            matching_objects = self.get_all()
            serializer = self.SERIALIZER(matching_objects, many=True)
            return Response(serializer.data)

    def put(self, request, format=None):
        id = request.data.get(self.ID_NAME, None)
        try:
            matching_object = self.get_object(id)
        except self.MODEL.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        serializer = self.SERIALIZER(matching_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        id = request.data.get(self.ID_NAME, None)
        matching_object = self.get_object(id)
        matching_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)