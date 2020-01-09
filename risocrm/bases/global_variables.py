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

OPERATOR_CHOICES = [
    ('exact', 'Exact'),
    ('iexact', 'Exact case-insensitive'),
    ('contains', 'Contains'),
    ('icontains', 'Contains case-insensitive'),
    ('in', 'In'),
    ('gt', 'Greater than'),
    ('gte', 'Greater than equal'),
    ('lt', 'Less than'),
    ('lte', 'Less than equal'),
    ('startswith', 'Start with'),
    ('istartswith', 'Start with case-insensitive'),
    ('endswith', 'End with'),
    ('iendswith', 'End with case-insensitive'),
    ('isnull', 'Is Null')
]


NOTICE_CHOICES = (
    ('flaticon2-gear', 'System'),
    ('flaticon2-user', 'Customer'),
    ('flaticon2-send', 'Email'),
    ('flaticon2-calendar-1', 'Event'),
    ('flaticon2-indent-dots', 'Task'),

)


CHART_CHOICES = (
    ('column', 'Column Chart'),
    ('line', 'Line Chart'),
    ('column-line', 'Column Line Chart'),
    ('pie', 'Pie Chart'),
    ('radar', 'Radar Chart'),
    ('table', 'Table'),
)


RELATION_TYPE = ['ForeignKey', 'ManyToManyField', 'OneToOneField']
ON_DELETE_TYPE = ['CASCADE', 'PROTECT', 'SET_NULL', 'SET_DEFAULT', 'SET', 'DO_NOTHING']
STRING_TYPE = ['CharField', 'TextField']
BOOL_TYPE = ['BooleanField', 'NullBooleanField']
TIME_TYPE = ['DateField', 'DateTimeField', 'TimeField']
NUMBER_TYPE = ['BigIntegerField', 'IntegerField', 'PositiveIntegerField',
               'PositiveSmallIntegerField', 'SmallIntegerField', 'DecimalField', 'FloatField']
FILE_TYPE = ['FileField', 'ImageField']
ALL_TYPE = RELATION_TYPE + STRING_TYPE + BOOL_TYPE + TIME_TYPE + NUMBER_TYPE + FILE_TYPE

FIELD_TYPE_CHOICES = (
    ('ForeignKey', 'ForeignKey'),
    ('ManyToManyField', 'ManyToManyField'),
    ('OneToOneField', 'OneToOneField'),
    ('CharField', 'CharField'),
    ('TextField', 'TextField'),
    ('BooleanField', 'BooleanField'),
    ('NullBooleanField', 'NullBooleanField'),
    ('DateField', 'DateField'),
    ('DateTimeField', 'DateTimeField'),
    ('TimeField', 'TimeField'),
    ('BigIntegerField', 'BigIntegerField'),
    ('IntegerField', 'IntegerField'),
    ('PositiveIntegerField', 'PositiveIntegerField'),
    ('PositiveSmallIntegerField', 'PositiveSmallIntegerField'),
    ('SmallIntegerField', 'SmallIntegerField'),
    ('DecimalField', 'DecimalField'),
    ('FloatField', 'FloatField'),
    ('FileField', 'FileField'),
    ('ImageField', 'ImageField'),
)

ON_DELETE_CHOICES = (
    ('CASCADE', 'CASCADE'),
    ('PROTECT', 'PROTECT'),
    ('SET_NULL', 'SET_NULL'),
    ('DO_NOTHING', 'DO_NOTHING')
)
