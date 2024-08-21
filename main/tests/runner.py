from django.conf import settings
from django.test.runner import DiscoverRunner


class Runner(DiscoverRunner):
    def run_tests(self, test_labels, **kwargs):
        result = super().run_tests(test_labels, **kwargs)
        settings.CACHES["default"]["LOCATION"] = (
            f"{settings.CACHES["default"]["LOCATION"]}/1"
        )
        return result
