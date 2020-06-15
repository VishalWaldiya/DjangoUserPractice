from django import forms
from django.utils.translation import gettext_lazy as _

from articles.models import Article

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class ArticleForm(forms.Form):
    name = forms.CharField(
        label = "Title of Article",
        max_length = 100,
        required = True,
    )
    description = forms.Textarea(
        # label = "Enter Article Text"
    )

    tags = forms.CharField(
        label = "Enter Tags Seperated by ','",
        max_length=500
    )

    category = forms.CharField(
        label = "Enter Category",
        max_length=50
    )








































# class ArticleForm(forms.ModelForm):
#     """Form definition for Article."""

#     # helper = FormHelper()
#     # helper.layout = Layout(
#     #                     ButtonHolder(
#     #                                 Submit('submit', 'Submit', css_class='button white')
#     #                             )
#     # )

#     class Meta:
#         """Meta definition for Articleform."""

#         model = Article
#         # fields = '__all__'
#         exclude = ('UserInfo',)

#         labels = {
#             'name': _('Topic'),
#             'tags': _('Tags'),
#             'category': _('Category'),
#         }
#         help_texts = {
#             'name': _('Enter Article Topic.'),
#             'tags': _('Enter Tags seperated by ",".'),
#             'category': _('Select Category'),
#         }
#         error_messages = {
#             'name': {
#                 'max_length': _("This Article topic's name is too long."),
#             },
#             'tags': {
#                 'max_length': _("This Article topic's name is too long."),
#             },
#         }
