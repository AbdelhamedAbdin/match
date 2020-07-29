from django.shortcuts import render, redirect
from match.models import Main
from .models import Statistics
from .forms import StaticForm
from django.db.models import F


def player_statics(request, pk):
    form = StaticForm()
    statics = Statistics.objects.filter(main_id=pk)
    main_pk = Main.objects.get(pk=pk)
    if request.method == 'POST':
        if 'short_pos' in request.POST:
            form = StaticForm(request.POST, instance=main_pk.statistics)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.short_pass += 1
                instance.save()
                # static = Statistics.objects.filter(main_id=pk).update(short_pass=form.cleaned_data['short_pass'] + 1)
                # static = Statistics.objects.filter(main_id=pk).update(short_pass=F('short_pass') + 1)
    
    context = {'form': form, 'statics': statics, 'main_pk': main_pk}
    return render(request, 'match_statics/player_statics.html', context)
