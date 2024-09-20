from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like  # Make sure to import Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification  # Import Notification

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def like_post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # Correct way to retrieve the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create a notification for the post author
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({"message": "Post liked."})
        return Response({"message": "You have already liked this post."})

    def unlike_post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # Correct way to retrieve the post
        like = Like.objects.filter(user=request.user, post=post)

        if like.exists():
            like.delete()
            return Response({"message": "Post unliked."})
        return Response({"message": "You have not liked this post."})

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)