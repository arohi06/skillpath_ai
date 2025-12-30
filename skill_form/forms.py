from django import forms

class SkillForm(forms.Form):
    degree = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'e.g., BSc Computer Science', 'class': 'box'})
    )
    skills = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Comma separated skills', 'class': 'box'})
    )
    end_goal = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'e.g., Become a data engineer', 'class': 'box'})
    )
    time_available = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'e.g., 10 hours/week', 'class': 'box'})
    )