from rest_framework import serializers
from .models import Element, Group


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('parent_group', 'group_icon', 'group_name', 'group_description',
                  'child_groups_count', 'child_groups_list', 'child_elements_count', 'child_elements_list')

    def save(self, **kwargs):
        node = Group.objects.all()
        if len(node) > 0:
            if self.validated_data['parent_group'] is None:
                raise serializers.ValidationError("Chose parent group")
            Group.objects.get(self.validated_data['parent_group'].pk).add_child(parent_group=self.validated_data['parent_group'],
                                                                                group_name=self.validated_data['group_name'],
                                                                                group_icon=self.validated_data['group_icon'],
                                                                                group_description=self.validated_data['group_description'])
        else:
            Group.add_root(group_name=self.validated_data['group_name'],
                           group_icon=self.validated_data['group_icon'],
                           group_description=self.validated_data['group_description']
                           )


class ElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Element
        fields = ('parent_group', 'element_icon', 'element_name', 'element_description', 'date_created')


class ChildGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('parent_group', 'group_icon', 'group_name', 'group_description',
                  'child_groups_count', 'child_groups_list', 'child_elements_count', 'child_elements_list')


class ChildElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Element
        fields = ('parent_group', 'element_icon', 'element_name', 'element_description', 'date_created')