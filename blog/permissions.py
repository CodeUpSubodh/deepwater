from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.core.exceptions import PermissionDenied


class ArticlePermissionMixin:
    def has_permission(self):
        article = self.get_object()
        return self.request.user == article.created_by or self.request.user.has_perm('blog.can_publish_article')

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)