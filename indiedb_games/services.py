from django.core.paginator import (Paginator,
                                   EmptyPage,
                                   PageNotAnInteger)


def paginate_objects(request, objects):
    paginator = Paginator(objects, 4)
    page = request.GET.get('page')

    try:
        paginated_objects = paginator.page(page)

    except PageNotAnInteger:
        paginated_objects = paginator.page(1)

    except EmptyPage:
        paginated_objects = paginator.page(paginator.num_pages)

    return paginated_objects


def generate_additional_genre_url(genre: str):
    if genre:
        genre_additional_url = f'&genre={genre}'
    else:
        genre_additional_url = ''

    return genre_additional_url
