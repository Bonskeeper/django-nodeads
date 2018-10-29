from rest_framework import viewsets
from .serializers import ElementSerializer, GroupSerializer, ChildGroupSerializer, ChildElementSerializer
from .models import Element, Group


class ElementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows elements to be viewed or edited.
    """
    queryset = Element.objects.filter(moderation=True).order_by('id')
    serializer_class = ElementSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ChildGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = ChildGroupSerializer

    def get_queryset(self):
        parent_group = self.request.path.split('/')[2]
        node_object = Group.objects.filter(pk=parent_group).first()
        queryset = node_object.get_children()
        return queryset


class ChildElementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that display child elements of choosen group.
    """
    serializer_class = ChildElementSerializer

    def get_queryset(self):
        parent_group = self.request.path.split('/')[2]
        queryset = Element.objects.filter(parent_group=parent_group, moderation=True).order_by('id')
        return queryset