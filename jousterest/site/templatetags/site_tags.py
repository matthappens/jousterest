from django import template
register = template.Library()


@register.filter(name='add_css')
def add_css(field, css):
    return field.as_widget(attrs={"class": css})


@register.assignment_tag
def get_next_page(page, num_pages):
    if int(page) < int(num_pages):
        return int(page)+1
    else:
        return int(num_pages)


@register.assignment_tag
def get_previous_page(page):
    if int(page) > 1:
        return int(page)-1
    else:
        return 1
