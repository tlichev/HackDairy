from django.shortcuts import render

# Create your views here.
# themes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Theme
from .forms import CommentForm, ThemeForm


def theme_list(request):
    themes = Theme.objects.all()
    paginator = Paginator(themes, 10)  # Показва по 10 теми на страница

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'themes/theme_list.html', {'page_obj': page_obj})


def theme_detail(request, pk):
    theme = get_object_or_404(Theme, pk=pk)
    comments = theme.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.theme = theme
            comment.author = request.user
            comment.save()
            messages.success(request, 'Вашият коментар беше добавен успешно!')
            return redirect('theme_detail', pk=theme.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'themes/theme_detail.html', {
        'theme': theme,
        'comments': comments,
        'comment_form': comment_form,
    })





@login_required
def theme_create(request):
    if request.method == 'POST':
        form = ThemeForm(request.POST, request.FILES)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.creator = request.user
            theme.save()
            messages.success(request, 'Темата беше създадена успешно!')
            return redirect('theme_detail', pk=theme.pk)
    else:
        form = ThemeForm()

    return render(request, 'themes/theme_form.html', {'form': form})


@login_required
def theme_edit(request, pk):
    theme = get_object_or_404(Theme, pk=pk)

    # Проверка дали потребителят е създател на темата
    if theme.creator != request.user:
        messages.error(request, 'Вие нямате права да редактирате тази тема!')
        return redirect('theme_detail', pk=theme.pk)

    if request.method == 'POST':
        form = ThemeForm(request.POST, request.FILES, instance=theme)
        if form.is_valid():
            form.save()
            messages.success(request, 'Темата беше обновена успешно!')
            return redirect('theme_detail', pk=theme.pk)
    else:
        form = ThemeForm(instance=theme)

    return render(request, 'themes/theme_form.html', {'form': form, 'edit_mode': True})


@login_required
def theme_delete(request, pk):
    theme = get_object_or_404(Theme, pk=pk)

    # Проверка дали потребителят е създател на темата
    if theme.creator != request.user:
        messages.error(request, 'Вие нямате права да изтриете тази тема!')
        return redirect('theme_detail', pk=theme.pk)

    if request.method == 'POST':
        theme.delete()
        messages.success(request, 'Темата беше изтрита успешно!')
        return redirect('index')

    return render(request, 'themes/theme_confirm_delete.html', {'theme': theme})
