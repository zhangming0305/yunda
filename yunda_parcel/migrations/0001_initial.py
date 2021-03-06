# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import yunda_parcel.models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yunda_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchAllowedParcelPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_price_eur', models.FloatField(verbose_name='Start price (EUR)')),
                ('start_weight_kg', models.FloatField(verbose_name='Start weight (KG)')),
                ('continuing_price_eur', models.FloatField(verbose_name='Continuing price (EUR)')),
                ('continuing_weight_kg', models.FloatField(verbose_name='Continuing weight (KG)')),
                ('volume_weight_rate', models.FloatField(verbose_name='Volume weight rate')),
                ('monthly_minimal_qty', models.IntegerField(default=0, verbose_name='Monthly minimal qty')),
                ('is_default', models.BooleanField(default=False)),
                ('branch', models.ForeignKey(to='yunda_user.Branch', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BranchParcelPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_price_eur', models.FloatField(verbose_name='Start price (EUR)')),
                ('start_weight_kg', models.FloatField(verbose_name='Start weight (KG)')),
                ('continuing_price_eur', models.FloatField(verbose_name='Continuing price (EUR)')),
                ('continuing_weight_kg', models.FloatField(verbose_name='Continuing weight (KG)')),
                ('volume_weight_rate', models.FloatField(verbose_name='Volume weight rate')),
                ('monthly_minimal_qty', models.IntegerField(default=0, verbose_name='Monthly minimal qty')),
                ('branch', models.ForeignKey(to='yunda_user.Branch', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CnCustomsTax',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cn_name', models.CharField(max_length=50, verbose_name='Chinese name')),
                ('en_name', models.CharField(max_length=50, verbose_name='English name', blank=True)),
                ('cn_custom_number', models.CharField(max_length=10, verbose_name='CN custom number')),
                ('hs_code', models.CharField(max_length=10, verbose_name='HS code', blank=True)),
                ('tax_rate', models.FloatField(verbose_name='Tax rate')),
                ('standard_unit_price_cny', models.FloatField(verbose_name='Standard unit price (CNY)')),
                ('charge_by_weight', models.BooleanField(default=False, verbose_name='Charge by weight')),
                ('forbidden_customs', models.CharField(help_text='Use comma between different customs.', max_length=500, verbose_name='Forbidden customs ', blank=True)),
                ('is_forbidden', models.NullBooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CnCustomsTaxCatalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cn_name', models.CharField(unique=True, max_length=50, verbose_name='Chinese name')),
                ('en_name', models.CharField(max_length=50, verbose_name='English name', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CnShenfengzheng',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=20, verbose_name='Shenfengzheng number')),
                ('name', models.CharField(max_length=20, verbose_name='Chinese name')),
                ('mobile', models.CharField(max_length=15, verbose_name='Mobilephone')),
                ('image', models.BinaryField(help_text=b'Jpeg format.', verbose_name='Image')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CustomerParcelPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_price_eur', models.FloatField(verbose_name='Start price (EUR)')),
                ('start_weight_kg', models.FloatField(verbose_name='Start weight (KG)')),
                ('continuing_price_eur', models.FloatField(verbose_name='Continuing price (EUR)')),
                ('continuing_weight_kg', models.FloatField(verbose_name='Continuing weight (KG)')),
                ('volume_weight_rate', models.FloatField(verbose_name='Volume weight rate')),
                ('branch_start_price_eur', models.FloatField(verbose_name='Branch start price (EUR)')),
                ('branch_start_weight_kg', models.FloatField(verbose_name='Branch start weight (KG)')),
                ('branch_continuing_price_eur', models.FloatField(verbose_name='Branch continuing price (EUR)')),
                ('branch_continuing_weight_kg', models.FloatField(verbose_name='Branch continuing weight (KG)')),
                ('branch_volume_weight_rate', models.FloatField(verbose_name='Branch volume weight rate')),
                ('monthly_minimal_qty', models.IntegerField(default=0, verbose_name='Monthly minimal qty')),
                ('branch', models.ForeignKey(to='yunda_user.Branch', null=True)),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DhlRetoureLabel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender_name', models.CharField(max_length=25, verbose_name='Sender name', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_name2', models.CharField(blank=True, max_length=25, verbose_name='Sender name2', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_company', models.CharField(blank=True, max_length=25, verbose_name='Sender company', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_state', models.CharField(blank=True, max_length=25, verbose_name='Sender state', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_city', models.CharField(max_length=25, verbose_name='Sender city', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_postcode', models.CharField(max_length=5, verbose_name='Sender postcode', validators=[yunda_parcel.models.field_validator_german_postcode])),
                ('sender_street', models.CharField(max_length=25, verbose_name='Sender street', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_add', models.CharField(blank=True, max_length=25, verbose_name='Sender street addition', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_hause_number', models.CharField(blank=True, max_length=10, verbose_name='Sender hause number', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_tel', models.CharField(max_length=15, verbose_name='Sender telephone')),
                ('sender_email', models.EmailField(blank=True, max_length=75, verbose_name='Sender email', validators=[django.core.validators.EmailValidator])),
                ('retoure_yde_number', models.CharField(max_length=12, blank=True)),
                ('tracking_number', models.CharField(max_length=12, verbose_name='Tracking number', blank=True)),
                ('is_deleted', models.NullBooleanField(default=False)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('pdf_file', models.BinaryField(blank=True)),
                ('printed_at', models.DateTimeField(null=True, verbose_name='Printed at')),
                ('created_at', models.DateTimeField()),
                ('payment_status', models.CharField(default=b'rl_pas_unpaid', max_length=60, choices=[(b'rl_pas_unpaid', 'Draft'), (b'rl_pas_paid', 'Paid'), (b'rl_pos_sender', 'At sender'), (b'rl_pos_op', 'At operation center'), (b'rl_pos_canceled', 'Canceled'), (b'others', 'Others')])),
                ('position_status', models.CharField(default=b'rl_pos_sender', max_length=60, choices=[(b'rl_pas_unpaid', 'Draft'), (b'rl_pas_paid', 'Paid'), (b'rl_pos_sender', 'At sender'), (b'rl_pos_op', 'At operation center'), (b'rl_pos_canceled', 'Canceled'), (b'others', 'Others')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DhlRetoureLabelStatusHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20, choices=[(b'payment_status', 'Payment status'), (b'position_status', 'Position status'), (b'others', 'Others')])),
                ('status', models.CharField(max_length=30, choices=[(b'rl_pas_unpaid', 'Draft'), (b'rl_pas_paid', 'Paid'), (b'rl_pos_sender', 'At sender'), (b'rl_pos_op', 'At operation center'), (b'rl_pos_canceled', 'Canceled'), (b'others', 'Others')])),
                ('create_at', models.DateTimeField()),
                ('dhl_retoure_label', models.ForeignKey(to='yunda_parcel.DhlRetoureLabel', null=True)),
                ('operator', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender_name', models.CharField(max_length=25, verbose_name='Sender name', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_name2', models.CharField(blank=True, max_length=25, verbose_name='Sender name2', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_company', models.CharField(blank=True, max_length=25, verbose_name='Sender company', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_state', models.CharField(blank=True, max_length=25, verbose_name='Sender state', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_city', models.CharField(max_length=25, verbose_name='Sender city', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_postcode', models.CharField(max_length=5, verbose_name='Sender postcode', validators=[yunda_parcel.models.field_validator_german_postcode])),
                ('sender_street', models.CharField(max_length=25, verbose_name='Sender street', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_add', models.CharField(blank=True, max_length=25, verbose_name='Sender street addition', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_hause_number', models.CharField(blank=True, max_length=10, verbose_name='Sender hause number', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_tel', models.CharField(max_length=15, verbose_name='Sender telephone')),
                ('sender_email', models.EmailField(blank=True, max_length=75, verbose_name='Sender email', validators=[django.core.validators.EmailValidator])),
                ('receiver_name', models.CharField(max_length=50, verbose_name='Receiver name', validators=[yunda_parcel.models.field_validator_only_chinese])),
                ('receiver_company', models.CharField(blank=True, max_length=50, verbose_name='Receiver company', validators=[yunda_parcel.models.field_validator_chinese_and_alphabeta])),
                ('receiver_province', models.CharField(max_length=20, verbose_name='Receiver province', validators=[yunda_parcel.models.field_validator_only_chinese])),
                ('receiver_city', models.CharField(blank=True, max_length=20, verbose_name='Receiver city', validators=[yunda_parcel.models.field_validator_only_chinese])),
                ('receiver_district', models.CharField(blank=True, max_length=20, verbose_name='Receiver district', validators=[yunda_parcel.models.field_validator_only_chinese])),
                ('receiver_postcode', models.CharField(max_length=6, verbose_name='Receiver postcode', validators=[yunda_parcel.models.field_validator_chinese_postcode])),
                ('receiver_address', models.CharField(max_length=50, verbose_name='Receiver address', validators=[yunda_parcel.models.field_validator_chinese_and_alphabeta])),
                ('receiver_address2', models.CharField(blank=True, max_length=50, verbose_name='Receiver address2', validators=[yunda_parcel.models.field_validator_chinese_and_alphabeta])),
                ('receiver_mobile', models.CharField(max_length=11, verbose_name='Receiver mobilephone', validators=[yunda_parcel.models.field_validator_chinese_mobile_phone])),
                ('receiver_email', models.EmailField(blank=True, max_length=75, verbose_name='Receiver email', validators=[django.core.validators.EmailValidator])),
                ('sender_country', models.CharField(default=b'CN', max_length=2, verbose_name='Receiver country')),
                ('ref', models.CharField(max_length=50, verbose_name='Ref number', blank=True)),
                ('weight_kg', models.FloatField(verbose_name='Weight (kg)', validators=[django.core.validators.MinValueValidator(0)])),
                ('length_cm', models.FloatField(verbose_name='Length (cm)', validators=[django.core.validators.MinValueValidator(0)])),
                ('width_cm', models.FloatField(verbose_name='Width (cm)', validators=[django.core.validators.MinValueValidator(0)])),
                ('height_cm', models.FloatField(verbose_name='Height (cm)', validators=[django.core.validators.MinValueValidator(0)])),
                ('real_weight_kg', models.FloatField(default=0, verbose_name='Real weight (kg)', blank=True)),
                ('real_length_cm', models.FloatField(default=0, verbose_name='Real Length (cm)', blank=True)),
                ('real_width_cm', models.FloatField(default=0, verbose_name='Real Width (cm)', blank=True)),
                ('real_height_cm', models.FloatField(default=0, verbose_name='Real Height (cm)', blank=True)),
                ('real_cn_customs_tax_cny', models.FloatField(null=True, verbose_name='Real customs tax (CNY)')),
                ('start_price_eur', models.FloatField(default=0, verbose_name='Start price (EUR)', blank=True)),
                ('start_weight_kg', models.FloatField(default=0.1, verbose_name='Start weight (KG)', blank=True)),
                ('continuing_price_eur', models.FloatField(default=0, verbose_name='Continuing price (EUR)', blank=True)),
                ('continuing_weight_kg', models.FloatField(default=0.1, verbose_name='Continuing weight (KG)', blank=True)),
                ('volume_weight_rate', models.FloatField(default=1, verbose_name='Volume weight rate', blank=True)),
                ('branch_start_price_eur', models.FloatField(default=0, verbose_name='Branch start price (EUR)', blank=True)),
                ('branch_start_weight_kg', models.FloatField(default=0.1, verbose_name='Branch start weight (KG)', blank=True)),
                ('branch_continuing_price_eur', models.FloatField(default=0, verbose_name='Branch continuing price (EUR)', blank=True)),
                ('branch_continuing_weight_kg', models.FloatField(default=0.1, verbose_name='Branch continuing weight (KG)', blank=True)),
                ('branch_volume_weight_rate', models.FloatField(default=1, verbose_name='Branch volume weight rate', blank=True)),
                ('tracking_number', models.CharField(max_length=15, verbose_name='Tracking number', blank=True)),
                ('tracking_number_created_at', models.DateTimeField(null=True)),
                ('yde_number', models.CharField(max_length=15, verbose_name='Tracking number', blank=True)),
                ('created_at', models.DateTimeField(null=True, verbose_name='Created at')),
                ('printed_at', models.DateTimeField(null=True, verbose_name='Printed at')),
                ('sender_pay_cn_customs', models.BooleanField(default=True)),
                ('payment_status', models.CharField(default=b'pr_pas_unpaid', max_length=60, choices=[(b'pr_pas_unpaid', 'Draft'), (b'pr_pas_paid', 'Paid'), (b'pr_pas_need_pay_rest', 'Need pay rest'), (b'pr_pas_need_pay_rest_complete', 'Complete'), (b'pr_pas_rest_auto_paid_complete', 'Complete'), (b'pr_pas_no_rest_complete', 'Complete'), (b'pr_cts_unpaid', 'Draft'), (b'pr_cts_sender_paid', 'Paid by sender'), (b'pr_cts_sender_pay_need_pay_rest', 'Need pay rest by sender'), (b'pr_cts_sender_pay_need_pay_rest_complete', 'Complete'), (b'pr_cts_sender_pay_complete', 'Complete'), (b'pr_cts_sender_pay_paid_back_complete', 'Complete'), (b'pr_cts_sender_pay_0tax', 'No Tax'), (b'pr_cts_sender_pay_0tax_need_pay_rest', 'Need pay'), (b'pr_cts_sender_pay_0tax_need_pay_rest_complete', 'Complete'), (b'pr_cts_sender_pay_0tax_rest_auto_paid_complete', 'Complete'), (b'pr_cts_receiver_pay', 'Receiver will pay'), (b'pr_cts_receiver_pay_need_pay', 'Need pay by receiver'), (b'pr_cts_receiver_pay_need_pay_complete', 'Complete'), (b'pr_cts_receiver_pay_0tax_complete', 'Complete'), (b'pr_pos_sender', 'At sender'), (b'pr_pos_way_from_sender_to_op', 'Way from sender to operation center'), (b'pr_pos_op', 'At operation center'), (b'pr_pos_waiting_to_export', 'Waiting to export'), (b'pr_pos_flied', 'Flied'), (b'pr_pos_destination_customs', 'At destination customs'), (b'pr_pos_destination_yunda', 'At destination yunda'), (b'pr_pos_canceled', 'Canceled'), (b'others', 'Others')])),
                ('position_status', models.CharField(default=b'pr_pos_sender', max_length=60, choices=[(b'pr_pas_unpaid', 'Draft'), (b'pr_pas_paid', 'Paid'), (b'pr_pas_need_pay_rest', 'Need pay rest'), (b'pr_pas_need_pay_rest_complete', 'Complete'), (b'pr_pas_rest_auto_paid_complete', 'Complete'), (b'pr_pas_no_rest_complete', 'Complete'), (b'pr_cts_unpaid', 'Draft'), (b'pr_cts_sender_paid', 'Paid by sender'), (b'pr_cts_sender_pay_need_pay_rest', 'Need pay rest by sender'), (b'pr_cts_sender_pay_need_pay_rest_complete', 'Complete'), (b'pr_cts_sender_pay_complete', 'Complete'), (b'pr_cts_sender_pay_paid_back_complete', 'Complete'), (b'pr_cts_sender_pay_0tax', 'No Tax'), (b'pr_cts_sender_pay_0tax_need_pay_rest', 'Need pay'), (b'pr_cts_sender_pay_0tax_need_pay_rest_complete', 'Complete'), (b'pr_cts_sender_pay_0tax_rest_auto_paid_complete', 'Complete'), (b'pr_cts_receiver_pay', 'Receiver will pay'), (b'pr_cts_receiver_pay_need_pay', 'Need pay by receiver'), (b'pr_cts_receiver_pay_need_pay_complete', 'Complete'), (b'pr_cts_receiver_pay_0tax_complete', 'Complete'), (b'pr_pos_sender', 'At sender'), (b'pr_pos_way_from_sender_to_op', 'Way from sender to operation center'), (b'pr_pos_op', 'At operation center'), (b'pr_pos_waiting_to_export', 'Waiting to export'), (b'pr_pos_flied', 'Flied'), (b'pr_pos_destination_customs', 'At destination customs'), (b'pr_pos_destination_yunda', 'At destination yunda'), (b'pr_pos_canceled', 'Canceled'), (b'others', 'Others')])),
                ('cn_tax_status', models.CharField(default=b'pr_cts_unpaid', max_length=60, choices=[(b'pr_pas_unpaid', 'Draft'), (b'pr_pas_paid', 'Paid'), (b'pr_pas_need_pay_rest', 'Need pay rest'), (b'pr_pas_need_pay_rest_complete', 'Complete'), (b'pr_pas_rest_auto_paid_complete', 'Complete'), (b'pr_pas_no_rest_complete', 'Complete'), (b'pr_cts_unpaid', 'Draft'), (b'pr_cts_sender_paid', 'Paid by sender'), (b'pr_cts_sender_pay_need_pay_rest', 'Need pay rest by sender'), (b'pr_cts_sender_pay_need_pay_rest_complete', 'Complete'), (b'pr_cts_sender_pay_complete', 'Complete'), (b'pr_cts_sender_pay_paid_back_complete', 'Complete'), (b'pr_cts_sender_pay_0tax', 'No Tax'), (b'pr_cts_sender_pay_0tax_need_pay_rest', 'Need pay'), (b'pr_cts_sender_pay_0tax_need_pay_rest_complete', 'Complete'), (b'pr_cts_sender_pay_0tax_rest_auto_paid_complete', 'Complete'), (b'pr_cts_receiver_pay', 'Receiver will pay'), (b'pr_cts_receiver_pay_need_pay', 'Need pay by receiver'), (b'pr_cts_receiver_pay_need_pay_complete', 'Complete'), (b'pr_cts_receiver_pay_0tax_complete', 'Complete'), (b'pr_pos_sender', 'At sender'), (b'pr_pos_way_from_sender_to_op', 'Way from sender to operation center'), (b'pr_pos_op', 'At operation center'), (b'pr_pos_waiting_to_export', 'Waiting to export'), (b'pr_pos_flied', 'Flied'), (b'pr_pos_destination_customs', 'At destination customs'), (b'pr_pos_destination_yunda', 'At destination yunda'), (b'pr_pos_canceled', 'Canceled'), (b'others', 'Others')])),
                ('fee_paid_eur', models.FloatField(default=0)),
                ('cn_tax_paid_cny', models.FloatField(default=0)),
                ('eur_to_cny_rate', models.FloatField(default=8)),
                ('is_delete', models.NullBooleanField(default=False)),
                ('branch', models.ForeignKey(to='yunda_user.Branch', null=True)),
                ('salesman', models.ForeignKey(related_name='Parcel.salesman', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParcelDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=50, verbose_name='Description', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('qty', models.FloatField(verbose_name='Qty', validators=[django.core.validators.MinValueValidator(0)])),
                ('item_net_weight_kg', models.FloatField(verbose_name='Item net weight (KG)', validators=[django.core.validators.MinValueValidator(0)])),
                ('item_price_eur', models.FloatField(verbose_name='Item price (EUR)', validators=[django.core.validators.MinValueValidator(0)])),
                ('original_country', models.CharField(default=b'DE', max_length=2, verbose_name='Original country')),
                ('cn_customs_tax', models.ForeignKey(to='yunda_parcel.CnCustomsTax', null=True)),
                ('parcel', models.ForeignKey(to='yunda_parcel.Parcel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParcelStatusHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20, choices=[(b'payment_status', 'Payment status'), (b'position_status', 'Position status'), (b'cn_tax_status', 'CN tax status'), (b'others', 'Others')])),
                ('status', models.CharField(max_length=60, choices=[(b'pr_pas_unpaid', 'Draft'), (b'pr_pas_paid', 'Paid'), (b'pr_pas_need_pay_rest', 'Need pay rest'), (b'pr_pas_need_pay_rest_complete', 'Complete'), (b'pr_pas_rest_auto_paid_complete', 'Complete'), (b'pr_pas_no_rest_complete', 'Complete'), (b'pr_cts_unpaid', 'Draft'), (b'pr_cts_sender_paid', 'Paid by sender'), (b'pr_cts_sender_pay_need_pay_rest', 'Need pay rest by sender'), (b'pr_cts_sender_pay_need_pay_rest_complete', 'Complete'), (b'pr_cts_sender_pay_complete', 'Complete'), (b'pr_cts_sender_pay_paid_back_complete', 'Complete'), (b'pr_cts_sender_pay_0tax', 'No Tax'), (b'pr_cts_sender_pay_0tax_need_pay_rest', 'Need pay'), (b'pr_cts_sender_pay_0tax_need_pay_rest_complete', 'Complete'), (b'pr_cts_sender_pay_0tax_rest_auto_paid_complete', 'Complete'), (b'pr_cts_receiver_pay', 'Receiver will pay'), (b'pr_cts_receiver_pay_need_pay', 'Need pay by receiver'), (b'pr_cts_receiver_pay_need_pay_complete', 'Complete'), (b'pr_cts_receiver_pay_0tax_complete', 'Complete'), (b'pr_pos_sender', 'At sender'), (b'pr_pos_way_from_sender_to_op', 'Way from sender to operation center'), (b'pr_pos_op', 'At operation center'), (b'pr_pos_waiting_to_export', 'Waiting to export'), (b'pr_pos_flied', 'Flied'), (b'pr_pos_destination_customs', 'At destination customs'), (b'pr_pos_destination_yunda', 'At destination yunda'), (b'pr_pos_canceled', 'Canceled'), (b'others', 'Others')])),
                ('create_at', models.DateTimeField()),
                ('operator', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('parcel', models.ForeignKey(to='yunda_parcel.Parcel', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParcelType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('code', models.CharField(default=b'default', max_length=50, verbose_name='Code')),
                ('description', models.TextField(verbose_name='Description')),
                ('to_country_code', models.CharField(help_text='ISO country code.', max_length=2, verbose_name='Destination country')),
                ('max_weight_kg', models.FloatField(verbose_name='Max weight (kg)')),
                ('need_shenfenzheng', models.BooleanField(default=True, verbose_name='Need shenfenzheng')),
                ('customs', models.CharField(help_text='Use comma between different customs.', max_length=500, verbose_name='Customs ')),
                ('has_customs_tax', models.BooleanField(default=True, verbose_name='Has CN customs tax')),
                ('start_price_eur', models.FloatField(verbose_name='Start price (EUR)')),
                ('start_weight_kg', models.FloatField(verbose_name='Start weight (KG)')),
                ('continuing_price_eur', models.FloatField(verbose_name='Continuing price (EUR)')),
                ('continuing_weight_kg', models.FloatField(verbose_name='Continuing weight (KG)')),
                ('volume_weight_rate', models.FloatField(verbose_name='Volume weight rate')),
                ('branch_start_price_eur', models.FloatField(verbose_name='Branch start price (EUR)')),
                ('branch_start_weight_kg', models.FloatField(verbose_name='Branch start weight (KG)')),
                ('branch_continuing_price_eur', models.FloatField(verbose_name='Branch continuing price (EUR)')),
                ('branch_continuing_weight_kg', models.FloatField(verbose_name='Branch continuing weight (KG)')),
                ('branch_volume_weight_rate', models.FloatField(verbose_name='Branch volume weight rate')),
                ('next_value', models.BigIntegerField(default=1, verbose_name='Next value')),
                ('prefix', models.CharField(max_length=10, blank=True)),
                ('digit_length', models.SmallIntegerField(default=0)),
                ('draft_next_value', models.BigIntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReceiverTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yde_number', models.CharField(max_length=15, verbose_name='YDE number', blank=True)),
                ('receiver_name', models.CharField(max_length=50, verbose_name='Receiver name', validators=[yunda_parcel.models.field_validator_only_chinese])),
                ('receiver_company', models.CharField(blank=True, max_length=50, verbose_name='Receiver company', validators=[yunda_parcel.models.field_validator_chinese_and_alphabeta])),
                ('receiver_province', models.CharField(max_length=20, verbose_name='Receiver province', validators=[yunda_parcel.models.field_validator_only_chinese])),
                ('receiver_city', models.CharField(blank=True, max_length=20, verbose_name='Receiver city', validators=[yunda_parcel.models.field_validator_only_chinese])),
                ('receiver_district', models.CharField(blank=True, max_length=20, verbose_name='Receiver district', validators=[yunda_parcel.models.field_validator_only_chinese])),
                ('receiver_postcode', models.CharField(max_length=6, verbose_name='Receiver postcode', validators=[yunda_parcel.models.field_validator_chinese_postcode])),
                ('receiver_address', models.CharField(max_length=50, verbose_name='Receiver address', validators=[yunda_parcel.models.field_validator_chinese_and_alphabeta])),
                ('receiver_address2', models.CharField(blank=True, max_length=50, verbose_name='Receiver address2', validators=[yunda_parcel.models.field_validator_chinese_and_alphabeta])),
                ('receiver_mobile', models.CharField(max_length=11, verbose_name='Receiver mobilephone', validators=[yunda_parcel.models.field_validator_chinese_mobile_phone])),
                ('receiver_email', models.EmailField(blank=True, max_length=75, verbose_name='Receiver email', validators=[django.core.validators.EmailValidator])),
                ('receiver_country', models.CharField(default=b'CN', max_length=2, verbose_name='Receiver country')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SenderTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yde_number', models.CharField(max_length=15, verbose_name='YDE number', blank=True)),
                ('sender_name', models.CharField(max_length=25, verbose_name='Sender name', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_name2', models.CharField(blank=True, max_length=25, verbose_name='Sender name2', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_company', models.CharField(blank=True, max_length=25, verbose_name='Sender company', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_state', models.CharField(blank=True, max_length=25, verbose_name='Sender state', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_city', models.CharField(max_length=25, verbose_name='Sender city', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_postcode', models.CharField(max_length=5, verbose_name='Sender postcode', validators=[yunda_parcel.models.field_validator_german_postcode])),
                ('sender_street', models.CharField(max_length=25, verbose_name='Sender street', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_add', models.CharField(blank=True, max_length=25, verbose_name='Sender street addition', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_hause_number', models.CharField(blank=True, max_length=10, verbose_name='Sender hause number', validators=[yunda_parcel.models.field_validator_only_alphabeta_num])),
                ('sender_tel', models.CharField(max_length=15, verbose_name='Sender telephone')),
                ('sender_email', models.EmailField(blank=True, max_length=75, verbose_name='Sender email', validators=[django.core.validators.EmailValidator])),
                ('sender_country', models.CharField(default=b'DE', max_length=2, verbose_name='Sender country')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='parcel',
            name='type',
            field=models.ForeignKey(to='yunda_parcel.ParcelType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='parcel',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customerparcelprice',
            name='parcel_type',
            field=models.ForeignKey(to='yunda_parcel.ParcelType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cncustomstax',
            name='categories',
            field=models.ManyToManyField(to='yunda_parcel.CnCustomsTaxCatalog', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='branchparcelprice',
            name='parcel_type',
            field=models.ForeignKey(to='yunda_parcel.ParcelType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='branchallowedparcelprice',
            name='parcel_type',
            field=models.ForeignKey(to='yunda_parcel.ParcelType'),
            preserve_default=True,
        ),
    ]
