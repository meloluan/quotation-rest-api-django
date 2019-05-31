from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Permitir que os usuários editem seu próprio perfil."""

    def has_object_permission(self, request, view, obj):
        """Verificar se o usuário está tentando editar seu próprio perfil."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """Permite que os usuários atualizem seu próprio status."""

    def has_object_permission(self, request, view, obj):
        """Verifica se o usuário está tentando atualizar seu próprio status."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
