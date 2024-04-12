from rest_framework.pagination import PageNumberPagination


class SchedulerPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 30


class ApplicantPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 30


class InterviewerPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 30


class ClientPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 30

class WorkExperiencePagination(PageNumberPagination):
    page_size = 20
    max_page_size = 30

class Guest_EnquiryPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 30