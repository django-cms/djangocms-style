# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re

from aldryn_client import forms


CLASS_NAME_FORMAT = re.compile(r'^\w[\w_-]*$')
TAG_TYPE_FORMAT = re.compile(r'^\w[\w\d]*$')


class ClassNamesField(forms.CharField):

    def clean(self, value):
        value = super(ClassNamesField, self).clean(value)
        class_names = filter(bool, map(lambda x: x.strip(), value.split(',')))
        for class_name in class_names:
            if not CLASS_NAME_FORMAT.match(class_name):
                raise forms.ValidationError(
                    '{0} is not a proper class name.'.format(class_name)
                )
        return ', '.join(class_names)


class TagTypesField(forms.CharField):

    def clean(self, value):
        value = super(TagTypesField, self).clean(value)
        tag_types = filter(bool, map(lambda x: x.strip(), value.split(',')))
        for tag_type in tag_types:
            if not TAG_TYPE_FORMAT.match(tag_type):
                raise forms.ValidationError(
                    '{0} does not look like a proper HTML tag.'.format(tag_type)
                )
        return ', '.join(tag_types)


class Form(forms.BaseForm):

    class_names = ClassNamesField('Class names', max_length=255)
    tag_types = TagTypesField('Tag types', max_length=255)

    def to_settings(self, data, settings):
        settings['ALDRYN_STYLE_CLASS_NAMES'] = [
            (class_name, class_name) for class_name in set(
                filter(bool, map(
                    lambda x: x.strip(), data['class_names'].split(','))))]
        settings['ALDRYN_STYLE_ALLOWED_TAGS'] = [
            (tag_type, tag_type) for tag_type in set(
                filter(bool, map(
                    lambda x: x.strip(), data['tag_types'].split(','))))]
        return settings
