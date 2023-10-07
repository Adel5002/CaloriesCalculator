from django import forms

GENDER = (
    (None, 'Ваш пол'),
    (1, 'Мужчина'),
    (2, 'Женщина'),
)

PHYSICAL_ACTIVITY = (
    (None, 'Ваша физическая активность'),
    (1, 'Легкая физическая активность'),
    (2, 'Средняя физическая активность'),
    (3, 'Высокая физическая активность'),
)

SURPLUS_DEFICIT = (
    (None, 'Ваша цель'),
    (1, 'Похудеть'),
    (2, 'Набрать массу'),
)

class CaloriesForm(forms.Form):
    weight = forms.IntegerField(
        label='Ваш вес в кг',
        error_messages={'required': 'Это поле обязательно для заполнения!'}
    )
    height = forms.IntegerField(
        label='Ваш рост см',
        error_messages={'required': 'Это поле обязательно для заполнения!'}
    )
    age = forms.IntegerField(
        label='Ваш возраст',
        error_messages={'required': 'Это поле обязательно для заполнения!'}
    )

    man_or_woman = forms.ChoiceField(
        choices=GENDER
    )

    physical_activity = forms.ChoiceField(
        choices=PHYSICAL_ACTIVITY
    )

    surplus_deficit = forms.ChoiceField(
        choices=SURPLUS_DEFICIT
    )

    surplus_deficit.widget.attrs.update({'class': 'text-center'})
    man_or_woman.widget.attrs.update({'class': 'text-center'})
    physical_activity.widget.attrs.update({'class': 'text-center'})

