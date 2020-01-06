"""
    System command
"""

from io import StringIO

from django.core.management import call_command


def Make_Migration():
    """Execute makemigration command"""
    out = StringIO()
    try:
        call_command('makemigrations', stdout=out)
    except EOFError as e:
        # Shell display choice for default value
        return 'Some "Field" is missing default value'
    return out.getvalue()


def Migrate():
    """Execute migrate command"""
    out = StringIO()
    call_command('migrate', stdout=out)
    return out.getvalue()
