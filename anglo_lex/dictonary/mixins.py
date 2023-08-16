from django.views.generic.detail import SingleObjectMixin


class GetObjectMixin(SingleObjectMixin):
    model = None

    def get_object(self, queryset=None, **kwargs):
        obj = self.model.objects.get(title=self.kwargs['wordbook_title'])
        return obj