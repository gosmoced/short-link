from django.shortcuts import redirect, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LinkSerializer
from .models import Link, Click
from django.http import HttpResponse


class CreateLink(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetLink(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_link = Link.objects.filter(user=request.user).order_by('-id')
        serializer = LinkSerializer(user_link, many=True)
        return Response(serializer.data)


class DeleteLink(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, pk):
        link = get_object_or_404(Link, pk=pk, user=request.user)
        link.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def redirect_link(request, incoming_title):
    try:
        link = Link.objects.get(title=incoming_title)

        Click.objects.create(
            link=link,
            ip_address=get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', '')[:500]
        )

        link.clicks += 1
        link.save()

        return redirect(link.url)
    except Link.DoesNotExist:
        return HttpResponse("Ссылка не найдена", status=404)

