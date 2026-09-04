from django.http import JsonResponse, FileResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .models import Project, Task, Comment, Notification

import os
import json


# ==================== HOME ====================

def home(request):
    frontend_path = os.path.join(settings.BASE_DIR, "index.html")

    if os.path.exists(frontend_path):
        return FileResponse(
            open(frontend_path, "rb"),
            content_type="text/html"
        )

    return JsonResponse({
        "message": "Frontend index.html not found"
    })


# ==================== REGISTER ====================

@csrf_exempt
def register_user(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "POST method required"},
            status=405
        )

    try:
        data = json.loads(request.body)

        username = data.get("username")
        email = data.get("email", "")
        password = data.get("password")

        if not username or not password:
            return JsonResponse(
                {"error": "Username and password are required"},
                status=400
            )

        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {"error": "Username already exists"},
                status=400
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return JsonResponse({
            "message": "Registration successful",
            "username": user.username
        })

    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=400
        )


# ==================== LOGIN ====================

@csrf_exempt
def login_user(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "POST method required"},
            status=405
        )

    try:
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user is None:
            return JsonResponse(
                {"error": "Invalid username or password"},
                status=401
            )

        return JsonResponse({
            "success": True,
            "username": user.username,
            "message": "Login successful"
        })

    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=400
        )


# ==================== PROJECTS ====================

@csrf_exempt
def projects(request):

    if request.method == "GET":

        project_list = []

        for project in Project.objects.all():

            project_list.append({
                "id": project.id,
                "name": project.name,
                "description": project.description,
                "owner": project.owner.username,
                "created_at": project.created_at
            })

        return JsonResponse(project_list, safe=False)


    if request.method == "POST":

        try:
            data = json.loads(request.body)

            name = data.get("name")
            description = data.get("description", "")
            username = data.get("username", "rishika_new")

            if not name:
                return JsonResponse(
                    {"error": "Project name is required"},
                    status=400
                )

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return JsonResponse(
                    {"error": "User not found"},
                    status=404
                )

            project = Project.objects.create(
                name=name,
                description=description,
                owner=user
            )

            project.members.add(user)

            return JsonResponse({
                "message": "Project created successfully",
                "id": project.id,
                "name": project.name
            })

        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status=400
            )


    return JsonResponse(
        {"error": "Method not allowed"},
        status=405
    )


# ==================== TASKS ====================

@csrf_exempt
def tasks(request):

    if request.method == "GET":

        task_list = []

        for task in Task.objects.all():

            task_list.append({
                "id": task.id,
                "project": task.project.id,
                "project_name": task.project.name,
                "title": task.title,
                "description": task.description,
                "assigned_to": (
                    task.assigned_to.username
                    if task.assigned_to else None
                ),
                "status": task.status,
                "priority": task.priority,
                "due_date": task.due_date,
                "created_at": task.created_at,
                "updated_at": task.updated_at
            })

        return JsonResponse(task_list, safe=False)


    if request.method == "POST":

        try:
            data = json.loads(request.body)

            project_id = data.get("project") or data.get("project_id")
            title = data.get("title")
            description = data.get("description", "")
            status = data.get("status", "todo")
            priority = data.get("priority", "medium")
            due_date = data.get("due_date")

            if not project_id or not title:
                return JsonResponse(
                    {
                        "error":
                        "Project ID and task title are required"
                    },
                    status=400
                )

            try:
                project = Project.objects.get(id=project_id)
            except Project.DoesNotExist:
                return JsonResponse(
                    {"error": "Project not found"},
                    status=404
                )

            task = Task.objects.create(
                project=project,
                title=title,
                description=description,
                status=status,
                priority=priority,
                due_date=due_date
            )

            return JsonResponse({
                "message": "Task created successfully",
                "id": task.id,
                "title": task.title
            })

        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status=400
            )


    return JsonResponse(
        {"error": "Method not allowed"},
        status=405
    )


# ==================== COMMENTS ====================

@csrf_exempt
def comments(request):

    if request.method == "GET":

        comment_list = []

        for comment in Comment.objects.all():

            comment_list.append({
                "id": comment.id,
                "task": comment.task.id,
                "task_title": comment.task.title,
                "user": comment.user.username,
                "content": comment.content,
                "created_at": comment.created_at
            })

        return JsonResponse(comment_list, safe=False)


    if request.method == "POST":

        try:
            data = json.loads(request.body)

            task_id = data.get("task_id")
            content = data.get("content")
            username = data.get("username", "rishika_new")

            if not task_id or not content:
                return JsonResponse(
                    {
                        "error":
                        "Task ID and comment are required"
                    },
                    status=400
                )

            try:
                task = Task.objects.get(id=task_id)
                user = User.objects.get(username=username)
            except Task.DoesNotExist:
                return JsonResponse(
                    {"error": "Task not found"},
                    status=404
                )
            except User.DoesNotExist:
                return JsonResponse(
                    {"error": "User not found"},
                    status=404
                )

            comment = Comment.objects.create(
                task=task,
                user=user,
                content=content
            )

            return JsonResponse({
                "message": "Comment added successfully",
                "id": comment.id
            })

        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status=400
            )


    return JsonResponse(
        {"error": "Method not allowed"},
        status=405
    )


# ==================== NOTIFICATIONS ====================

@csrf_exempt
def notifications(request):

    if request.method == "GET":

        notification_list = []

        for notification in Notification.objects.all():

            notification_list.append({
                "id": notification.id,
                "user": notification.user.username,
                "message": notification.message,
                "is_read": notification.is_read,
                "created_at": notification.created_at
            })

        return JsonResponse(
            notification_list,
            safe=False
        )


    if request.method == "POST":

        try:
            data = json.loads(request.body)

            username = data.get(
                "username",
                "rishika_new"
            )

            message = data.get("message")

            if not message:
                return JsonResponse(
                    {"error": "Message is required"},
                    status=400
                )

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return JsonResponse(
                    {"error": "User not found"},
                    status=404
                )

            notification = Notification.objects.create(
                user=user,
                message=message
            )

            return JsonResponse({
                "message": "Notification created successfully",
                "id": notification.id
            })

        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status=400
            )


    return JsonResponse(
        {"error": "Method not allowed"},
        status=405
    )


# ==================== WEBSOCKET TEST ====================

def websocket_test(request):

    return JsonResponse({
        "message": "WebSocket test endpoint is available"
    })