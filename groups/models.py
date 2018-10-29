from django.db import models
from treebeard.mp_tree import MP_Node
from django_api.settings import HOSTNAME



class Group(MP_Node):
    parent_group = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    group_icon = models.ImageField(default='default_group.png', upload_to='groups_icons')
    group_name = models.CharField(max_length=64)
    group_description = models.TextField(max_length=512, null=True, blank=True)

    @property
    def child_groups_count(self):
        total_gr = self.get_children_count()
        return total_gr

    @property
    def child_groups_list(self):
        print({})
        groups_json = {"child-groups": "{hostname}groups/{pk}/child_groups/".format(hostname=HOSTNAME, pk=self.pk)}
        return groups_json

    @property
    def child_elements_count(self):
        total_el = Element.objects.filter(parent_group=self.pk, moderation=True).count()
        return total_el

    @property
    def child_elements_list(self):
        child_elements = {"child-elements": "{hostname}elements/{pk}/child_elements/".format(hostname=HOSTNAME, pk=self.pk)}
        return child_elements

    def __str__(self):
        return f'{self.group_name} Group'


class Element(models.Model):
    parent_group = models.ForeignKey(
        Group,
        related_name='groups',
        on_delete=models.CASCADE
    )
    element_icon = models.ImageField(default='default_element.png', upload_to='elements_icons')
    element_name = models.CharField(max_length=64)
    element_description = models.TextField(max_length=512, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    moderation = models.BooleanField(null=True, default=None)

    def __str__(self):
        return f'{self.element_name} Element'
