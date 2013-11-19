# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a PDB file to upload',
        help_text='(max. 42MB)'
    )
