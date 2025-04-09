# comments/views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Comment
from .forms import CommentForm
from ..themes.models import Theme


@login_required
def comment_create(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.theme = theme
            comment.author = request.user
            comment.save()
            messages.success(request, 'Вашият коментар беше добавен успешно!')

    return redirect('theme_detail', pk=theme.pk)


@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    theme_pk = comment.theme.pk

    # Проверка дали потребителят е автор на коментара
    if comment.author != request.user:
        messages.error(request, 'Вие нямате права да изтриете този коментар!')
        return redirect('theme_detail', pk=theme_pk)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Коментарът беше изтрит успешно!')

    return redirect('theme_detail', pk=theme_pk)


@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    theme_pk = comment.theme.pk

    # Проверка дали потребителят е автор на коментара
    if comment.author != request.user:
        messages.error(request, 'Вие нямате права да редактирате този коментар!')
        return redirect('theme_detail', pk=theme_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Коментарът беше обновен успешно!')
            return redirect('theme_detail', pk=theme_pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'comments/comment_edit.html', {
        'form': form,
        'comment': comment,
        'theme': comment.theme
    })