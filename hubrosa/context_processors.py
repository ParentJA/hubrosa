__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Local imports...
import settings


def cdn_imports(request):
    return {
        'BOOTSTRAP_CSS_URL': getattr(settings, 'BOOTSTRAP_CSS_URL'),
        'BOOTSTRAP_JS_URL': getattr(settings, 'BOOTSTRAP_JS_URL'),
        'JQUERY_URL': getattr(settings, 'JQUERY_URL'),
        'ANGULAR_JS_URL': getattr(settings, 'ANGULAR_JS_URL'),
    }