from django.views.generic import FormView, TemplateView
from django.urls import reverse

from .forms import CaloriesForm


class CaloriesFormView(FormView):
    template_name = 'calculation/caloriesform.html'
    form_class = CaloriesForm

    def form_valid(self, form):
        # Getting the input data
        self.request.session['weight'] = form.cleaned_data['weight']
        self.request.session['height'] = form.cleaned_data['height']
        self.request.session['age'] = form.cleaned_data['age']
        self.request.session['man_or_woman'] = form.cleaned_data['man_or_woman']
        self.request.session['physical_activity'] = form.cleaned_data['physical_activity']
        self.request.session['surplus_deficit'] = form.cleaned_data['surplus_deficit']

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Passing the input data
        weight = self.request.session.get('weight') or 0
        height = self.request.session.get('height') or 0
        age = self.request.session.get('age') or 0
        man_or_woman = self.request.session.get('man_or_woman')
        physical_activity = self.request.session.get('physical_activity')
        surplus_deficit = self.request.session.get('surplus_deficit')

        # Calculating the daily calorie allowance for both sexes
        man = (weight * 10) + (height * 6.25) - (age * 5) + 5
        woman = (weight * 10) + (height * 6.25) - (age * 5) - 161
        daily_rate = man if man_or_woman == '1' else woman

        # Determination of human activity
        low = daily_rate * 1.2
        medium = daily_rate * 1.46
        high = daily_rate * 1.64
        daily_activity = (
            low if physical_activity == '1' else
            high if physical_activity == '3' else medium)

        # Calculation based on a person's goal to lose weight or gain weight
        goal = (
            round(daily_activity - (daily_activity * 0.2), 2) if surplus_deficit == '1' else
            round(daily_activity + (daily_activity * 0.1), 2))

        context['total'] = goal
        return context

    def get_success_url(self):
        return reverse('main')


class AboutMe(TemplateView):
    template_name = 'about_me/about_me.html'