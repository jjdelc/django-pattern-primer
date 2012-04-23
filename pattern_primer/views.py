from os import listdir
from os.path import join
from urlparse import urljoin

from django.conf import settings
from django.views.generic.base import TemplateView


class PatternsView(TemplateView):
    template_name = 'pattern_primer/index.html'

    PATTERN_EXTENSION = 'html'

    def get_patterns(self):
        path = join(settings.MEDIA_ROOT, 'patterns')
        pattern_list = []

        for fname in listdir(path):
            if fname.endswith(self.PATTERN_EXTENSION):
                pattern_filename = join(path, fname)
                content = open(pattern_filename).read()
                pattern_list.append({
                    'content': content,
                    'filename': fname,
                    'url': urljoin(settings.MEDIA_URL, 'patterns/%s' % fname)
                })

        return pattern_list


    def get_context_data(self, **kwargs):
        ctx = super(PatternsView, self).get_context_data(**kwargs)
        ctx['patterns'] = self.get_patterns()
        ctx['global_css'] = settings.PATTERN_PRIMER_GLOBAL_CSS
        return ctx
