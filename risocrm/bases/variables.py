"""
    Constant List
"""
BASE_MODEL = [
    'User',
    'Permission',
    'Group',
    'ContentType',
    'Session',
    'Site',
    'LogEntry',

    'EmailAddress',
    'EmailConfirmation',

    'SocialAccount',
    'SocialApp',
    'SocialToken',

    'CrontabSchedule',
    'IntervalSchedule',
    'PeriodicTask',
    'PeriodicTasks',
    'SolarSchedule',
    'ClockedSchedule',

    'Filter',
    'FilterDetail',

    'Notice',

    'Tile',
    'TileDetail',

    'SystemConfig',
    'FilterConfig',

    'ExternalConfig',
    'ReportConfig',
    'FieldConfig',

    'Dynafield',

    'PushInformation',
    'SubscriptionInfo',

    'Choice',
    'ChoiceDetail',
]

ADDED_APP = [
    'Activity',
    'Note',
]

EXCLUDE_TYPE = [
    'ManyToManyRel',
]

BASE_USER = [
    'logentry',
    'emailaddress',
    'socialaccount',
    'id',
    'password',
    'last_login',
    'is_superuser',
    'username',
    'first_name',
    'last_name',
    'email',
    'is_staff',
    'is_active',
    'date_joined',
    'groups',
    'user_permissions'
]

BASE_FIELD = [
    'id',
    'time_created',
    'time_modified',
    'creator',
    'last_modified_by',
]


RELATION_TYPE = ['ForeignKey', 'ManyToManyField', 'OneToOneField']
ON_DELETE_TYPE = ['CASCADE', 'PROTECT', 'SET_NULL', 'SET_DEFAULT', 'SET', 'DO_NOTHING']
STRING_TYPE = ['CharField', 'TextField']
BOOL_TYPE = ['BooleanField', 'NullBooleanField']
TIME_TYPE = ['DateField', 'DateTimeField', 'TimeField']
NUMBER_TYPE = ['BigIntegerField', 'IntegerField', 'PositiveIntegerField',
               'PositiveSmallIntegerField', 'SmallIntegerField', 'DecimalField', 'FloatField']
FILE_TYPE = ['FileField', 'ImageField']
ALL_TYPE = RELATION_TYPE + STRING_TYPE + BOOL_TYPE + TIME_TYPE + NUMBER_TYPE + FILE_TYPE
