from django.utils.translation import gettext_lazy as _


def error_handler(e):
    msg = ''
    if hasattr(e, 'detail'):
        if isinstance(e.detail, dict):
            for q in e.detail.items():
                msg += f"{q[1][0]} "
                break
        elif isinstance(e.detail, list):
            for q in e.detail:
                msg += f"{q} "
                break
        else:
            msg = str(e.detail)
    elif hasattr(e, 'message'):
        if isinstance(e.message, dict):
            for q in e.message.items():
                msg += f"{q[0]}: {q[1][0]} "
                break
        elif isinstance(e.message, list):
            for q in e.message:
                msg += f"{q} "
                break
        elif isinstance(e.message, str):
            msg = e.message
        else:
            msg = str(e)
    else:
        msg = str(e)
    return msg
