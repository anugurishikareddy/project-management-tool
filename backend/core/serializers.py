from rest_framework import serializers

from .models import (
    Project,
    Task,
    Comment,
    Notification,
)


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "owner",
            "members",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "owner",
            "created_at",
        ]


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "priority",
            "due_date",
            "created_at",
            "updated_at",
            "project",
            "assigned_to",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            "id",
            "content",
            "created_at",
            "task",
            "user",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "user",
        ]


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = [
            "id",
            "message",
            "is_read",
            "created_at",
            "user",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "user",
        ]