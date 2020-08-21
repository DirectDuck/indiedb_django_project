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

	return paginated_objects, page
