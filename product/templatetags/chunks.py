from django import template

register = template.Library()


@register.filter(name='chunks')
def chunks(chunk_list, chunk_size):
    i = 1
    chunk = []
    for ch in chunk_list:
        chunk.append(ch)
        if i == chunk_size:
            yield chunk
            chunk = []
            i = 0
        i += 1
    if chunk:
        yield chunk
