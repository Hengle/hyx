from restless.dj import DjangoResource
from restless.utils import format_traceback
from hyx.settings import PAGE_SIZE, PAGE_NUM
from django.core.paginator import Paginator
from hyx.settings import DEBUG
import sys


class Base(DjangoResource):

    def wrap_list_response(self,data):
        return dict(
            list=data
        )

    def is_authenticated(self):
        return True

    def is_debug(self):
        return DEBUG

    def build_error(self, err):
        """
        When an exception is encountered, this generates a JSON error message
        for display to the user.

        :param err: The exception seen. The message is exposed to the user, so
            beware of sensitive data leaking.
        :type err: Exception

        :returns: A response object
        """
        data = {
            'error': err.args[0],
        }

        if self.is_debug():
            # Add the traceback.

            data['traceback'] = format_traceback(sys.exc_info())

        body = self.serializer.serialize(data)
        status = getattr(err, 'status', 500)
        return self.build_response(body, status=status)

    def serialize_list(self, data):
        if self.request.GET.get('no_page', False):
            prepped_data = [self.prepare(item) for item in data]
            final_data = self.wrap_list_response(prepped_data)
            return self.serializer.serialize(final_data)
        else:

            page_size = self.request.GET.get('page_size', PAGE_SIZE)

            paginator = Paginator(data, page_size)  # get value data
            page_num = self.request.GET.get('page_num', PAGE_NUM)

            self.page = paginator.page(page_num)  # This django method takes care of the page number
            list = self.page.object_list
            prepped_data = [self.prepare(item) for item in list]
            final_data = self.wrap_list_response(prepped_data)
            final_data['page'] = dict(
                page_size=int(page_size),
                page_num=int(page_num),
                total=len(data)
            )

            return self.serializer.serialize(final_data)

