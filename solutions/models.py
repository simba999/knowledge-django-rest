from __future__ import unicode_literals
from django.db import models
from api.models import User, UserGroup, NotebookType, SolutionType

SOLUTION_STATUS_CHOICE = (
    (-1, "requested"),
    (1, "complete")
)

ENSEMBLE_CHOICE = (
    (-1, "requested"),
    (0, "complete"),
    (1, "none")
)

ENSEMBLE_FOREIGN_TYPE = (
    (0, "ensemble"),
    (1, "solution")
)

METAENSEMBLE_FOREIGN_TYPE = (
    (0, "ensemble"),
    (1, "solution")
)

PERFORMANCE_CHOICE = (
    (-1, "A/B"),
    (0, "onearmedbandit"),
    (1, "none")
)

LIBRARY_CHOICE = (
    (0, "notebook"),
    (1, "solution"),
    (2, "ensemble"),
    (3, "metaensemble"),
    (4, "dataset")
)

METAENSEMBLE_CHOICE = (
    (-1, "requested"),
    (0, "complete"),
    (1, "none")
)


class Solution(models.Model):
    """
        Solution model
    """
    Category = models.ForeignKey("Category", default=0)
    user = models.ForeignKey('User', default=0, related_name="user_solution")
    usergroup_ID = models.ForeignKey('UserGroup')
    type = models.ForeignKey('SolutionType', default=0)
    notebook = models.ForeignKey("Notebook", default=0, null=True, blank=True, related_name="solutions_notebook")
    library = models.ForeignKey("Library", null=True, blank=True)
    parent = models.ForeignKey("Solution", default=None, null=True, blank=True)
    price = models.ForeignKey("Price", blank=True, null=True, related_name="solutions_price")
    workflow_id = models.IntegerField(null=True)
    tags = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    rating = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    ensemble = models.ForeignKey("Ensemble", null=True, blank=True)
    metaensemble = models.ForeignKey("MetaEnsemble", null=True, blank=True)
    dataset = models.ForeignKey("Dataset", blank=True, null=True, related_name="solutions_dataset")
    author = models.ForeignKey('Author', blank=True, null=True, related_name="author_solution")
    status = models.IntegerField(choices=SOLUTION_STATUS_CHOICE, default=-1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=255, default=None, null=True, blank=True)
    timed = models.BooleanField(default=False)
    starting_time = models.DateTimeField(null=True, blank=True, default=None)
    ending_time = models.DateTimeField(null=True, blank=True, default=None)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Ensemble(models.Model):
    user = models.ForeignKey('User')
    usergroup = models.ForeignKey('UserGroup')
    parent = models.ForeignKey("Ensemble", null=True, blank=True)
    foreign_id = models.IntegerField(null=True, blank=True)
    foreign_type = models.IntegerField(choices=ENSEMBLE_FOREIGN_TYPE, default=0)
    performance = models.ForeignKey("Performance", default=0, null=True, related_name="ensembles_performance")
    notebook = models.ForeignKey("Notebook", null=True, blank=True, related_name="ensembles_notebook")
    dataset = models.ForeignKey("DataSet", null=True, blank=True, related_name="ensembles_dataset")
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=ENSEMBLE_CHOICE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Performance(models.Model):
    user = models.ForeignKey('User')
    usergroup = models.ForeignKey('UserGroup')
    solution = models.ForeignKey("Solution", null=True, blank=True)
    notebook = models.ForeignKey("Notebook", null=True, blank=True, related_name="performances_notebook")
    ensemble = models.ForeignKey("Ensemble", null=True, blank=True, related_name="performances_ensemble")
    results = models.BinaryField(null=True, blank=True)
    ABTest = models.IntegerField(default=1)
    PredictionAccuracyScore = models.IntegerField(default=0)
    ChangefromPrevious = models.IntegerField(default=0)
    PredictedImpact = models.IntegerField(default=0)
    RecordsinFile = models.IntegerField(default=0)
    DateRun = models.DateTimeField(null=True, blank=True)
    PerformanceResult = models.ForeignKey("PerformanceResult", null=True, blank=True)
    Date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Notebook(models.Model):
    """
    """
    solution = models.ForeignKey("Solution", blank=True, null=True, related_name="notebooks_solution")
    Category = models.ForeignKey("Category", default=0)
    parent = models.ForeignKey("Notebook", null=True, blank=True, default=None)
    type = models.ForeignKey(NotebookType, default=0, blank=True, null=True)
    jupyternotebook_ID = models.IntegerField(default=0)
    graphdatabase_ID = models.IntegerField(default=0)
    performance = models.ForeignKey("Performance", blank=True, null=True, related_name="notebooks_performance")
    price = models.ForeignKey("Price", blank=True, null=True, related_name="notebooks_price")
    accessparameters = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255)
    datasource = models.CharField(max_length=255)
    datafields = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    author = models.ForeignKey('User', default=None)
    ensemble = models.ForeignKey("Ensemble", null=True, blank=True, related_name="notebooks_ensemble")
    metaensemble = models.ForeignKey("MetaEnsemble", null=True, blank=True, related_name="notebooks_metaensemble")
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description


class MetaEnsemble(models.Model):
    id = models.BigIntegerField(primary_key=True)
    collection_id = models.IntegerField()
    foreign_id = models.IntegerField()
    foreign_type = models.IntegerField(choices=METAENSEMBLE_FOREIGN_TYPE, default=0)
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=METAENSEMBLE_CHOICE, default=1)
    notebook = models.ForeignKey("Notebook", default=0, null=True, related_name="metaensembles_notebook")
    dataset = models.ForeignKey("DataSet", default=0, null=True, related_name="metaensembles_dataset")
    ensemble = models.ForeignKey("Ensemble", default=0, null=True, related_name="metaensembles_ensemble")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class DataSet(models.Model):
    user = models.ForeignKey('User', related_name="user_dataset")
    solution = models.ForeignKey("Solution", null=True, blank=True, related_name="datasets_solution")
    Category = models.ForeignKey("Category")
    parent = models.ForeignKey("DataSet", null=True, blank=True)
    type = models.IntegerField(default=0)
    price = models.ForeignKey("Price", blank=True, null=True, related_name="datasets_price")
    accessparameters = models.CharField(max_length=255, null=True, blank=True)
    rating = models.IntegerField(default=0)
    description = models.CharField(max_length=255)
    datafields = models.BinaryField()
    author = models.ForeignKey(User, related_name="author_dataset")
    ensemble = models.ForeignKey("Ensemble", null=True, blank=True, related_name="datasets_ensemble")
    metaensemble = models.ForeignKey("MetaEnsemble", null=True, blank=True, related_name="datasets_metaensemble")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description


class DataField(models.Model):
    user = models.ForeignKey('User', null=True, blank=True, related_name="user_datafields")
    solution = models.ForeignKey("Solution", null=True, blank=True)
    dataset = models.ForeignKey("DataSet", default=0, null=True, blank=True)
    price = models.ForeignKey("Price", blank=True, null=True, related_name="prices_datafield")
    accessparameters = models.CharField(max_length=255, null=True, blank=True, default=None)
    description = models.CharField(max_length=255)
    datatype = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name="author_datafield")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description


class Price(models.Model):
    user = models.ForeignKey(User)
    solution = models.ForeignKey("Solution", null=True, blank=True, related_name="prices_solution")
    notebook = models.ForeignKey("Notebook", null=True, blank=True, related_name="prices_notebook")
    datafield = models.ForeignKey("DataField", null=True, blank=True, related_name="prices_datafield")
    dataset = models.ForeignKey("DataSet", null=True, blank=True, related_name="prices_dataset")
    price = models.FloatField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.pk

    def __str__(self):
        return self.pk


class PerformanceResult(models.Model):
    logfile = models.CharField(max_length=255, null=True, blank=True)
    outcome = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.pk

    def __str__(self):
        return self.pk


class Commission(models.Model):
    user = models.ForeignKey('User', null=True, blank=True, related_name="commissions_user")
    solution = models.ForeignKey('Solution', null=True, blank=True)
    commissions = models.DecimalField(max_digits=15, decimal_places=8, default=0)
    commisssion_accrued = models.DecimalField(max_digits=15, decimal_places=8, default=0)
    commission_rate = models.DecimalField(max_digits=15, decimal_places=8, default=0)
    product_sales = models.DecimalField(max_digits=15, decimal_places=8, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.pk

    def __str__(self):
        return self.pk


class recommendations(models.Model):
    solution = models.ForeignKey('Solution', null=True, blank=True)
    dataset = models.ForeignKey('DataSet', null=True, blank=True)
    ensemble = models.ForeignKey('Ensemble', null=True, blank=True)
    metaensemble = models.ForeignKey('MetaEnsemble', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Author(models.Model):
    author_name = models.CharField(max_length=255)
    author_id = models.IntegerField(primary_key=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    algo_metadata = models.ForeignKey('AlgoMetaData', null=True, blank=True, default=None)

    def __unicode__(self):
        return self.author_name

    def __str__(self):
        return self.author_name


class AlgoMetaData(models.Model):
    accuray = models.DecimalField(max_digits=18, decimal_places=5, default=0)
    test_points = models.DecimalField(max_digits=18, decimal_places=5, default=0)
    train_points = models.DecimalField(max_digits=18, decimal_places=5, default=0)
    bias = models.CharField(max_length=255, null=True, blank=True, default=None)
    variance = models.CharField(max_length=255, null=True, blank=True, default=None)


class Vertical(models.Model):
    name = models.CharField(max_length=55)
    user = models.ForeignKey('User', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=55)
    Category = models.ForeignKey("Category", null=True, blank=True)
    vertical = models.ForeignKey('Vertical', null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=55)
    parent = models.ForeignKey("Category", null=True, blank=True, default=None)
    vertical = models.ForeignKey("Vertical", null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class UserGroup(models.Model):
    name = models.CharField(max_length=55)
    category = models.ForeignKey('Category', default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(username=username)

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Email must be set!')
        user = self.model(email=email, username=username)
        # user.password = make_password(password)
        user.set_password(password)
        user.save(using=self._db)
        return user
        return None

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(models.Model):
    user = models.OneToOneField(AdminMember, on_delete=models.CASCADE)
    parent_id = models.IntegerField(default=0)
    group = models.ForeignKey('UserGroup', null=True, blank=True, default=None)
    tags = models.CharField(max_length=255, null=True, blank=True, default=None)
    # username = models.CharField(max_length=255, unique=True)
    # email = models.CharField(max_length=255, unique=True, default=None)
    # password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=255)
    image = models.CharField(max_length=255, null=True, blank=True, default=None)
    profile_name = models.CharField(max_length=255, null=True, blank=True, default=None)
    profile_description = models.CharField(max_length=255, null=True, blank=True, default=None)
    api_paypal = models.CharField(max_length=255, null=True, blank=True, default=0)
    api_payment = models.CharField(max_length=255, null=True, blank=True, default=0)
    commissions = models.DecimalField(max_digits=18, decimal_places=8, default=0)
    commission_rate = models.DecimalField(max_digits=18, decimal_places=8, default=0)
    commission_total = models.DecimalField(max_digits=18, decimal_places=8, default=0)
    commission_monthtodata = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    number_transaction = models.IntegerField(default=0)
    trend = models.IntegerField(default=0)
    potential_place = models.IntegerField(default=0)
    potential_earning = models.IntegerField(default=0)
    total_commission = models.IntegerField(default=0)
    total_purchase = models.FloatField(default=0)
    proj_earning_to_date = models.IntegerField(default=0)
    proj_earning_overall = models.IntegerField(default=0)
    proj_place_to_date = models.IntegerField(default=0)
    proj_place_overall = models.IntegerField(default=0)
    noteworthy = models.IntegerField(default=0)
    redeem_state = models.IntegerField(default=0)
    datascientist_reg = models.IntegerField(default=0)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)

    # objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return self.user.username

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.user.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# @receiver(post_save, sender=AdminMember)
# def create_user(sender, instance, created, **kwargs):
#     if created:
#         User.objects.create(user=instance)

# @receiver(post_save, sender=AdminMember)
# def save_user(sender, instance, **kwargs):
#     instance.user.save()


class NotebookType(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class SolutionType(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

