# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 18:07
from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import migrations, models
import django_countries.fields
import normandy.recipes.fields


class PercentField(models.FloatField):
    default_validators = [MinValueValidator(0), MaxValueValidator(100)]


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255, unique=True)),
                ('content', models.TextField()),
                ('content_hash', models.CharField(max_length=255, unique=True)),
                ('enabled', models.BooleanField(default=False)),
                ('locale', normandy.recipes.fields.LocaleField(blank=True, choices=[('st', 'Southern Sotho'), ('de-AT', 'German (Austria)'), ('bg', 'Bulgarian'), ('bn-BD', 'Bengali (Bangladesh)'), ('ne-NP', 'Nepali'), ('br', 'Breton'), ('th', 'Thai'), ('te', 'Telugu'), ('es-MX', 'Spanish (Mexico)'), ('km', 'Khmer'), ('dsb', 'Lower Sorbian'), ('ee', 'Ewe'), ('bm', 'Bambara'), ('ga', 'Irish'), ('de', 'German'), ('sr', 'Serbian'), ('fur-IT', 'Friulian'), ('lv', 'Latvian'), ('mai', 'Maithili'), ('vi', 'Vietnamese'), ('ro', 'Romanian'), ('dbg', 'Debug Robot'), ('es-AR', 'Spanish (Argentina)'), ('is', 'Icelandic'), ('it', 'Italian'), ('da', 'Danish'), ('af', 'Afrikaans'), ('sa', 'Sanskrit'), ('hu', 'Hungarian'), ('ml', 'Malayalam'), ('en-AU', 'English (Australian)'), ('bn-IN', 'Bengali (India)'), ('ko', 'Korean'), ('id', 'Indonesian'), ('ta-LK', 'Tamil (Sri Lanka)'), ('bs', 'Bosnian'), ('lij', 'Ligurian'), ('hr', 'Croatian'), ('fa', 'Persian'), ('sr-Cyrl', 'Serbian'), ('lg', 'Luganda'), ('hi', 'Hindi'), ('nl', 'Dutch'), ('ak', 'Akan'), ('brx', 'Bodo'), ('hy-AM', 'Armenian'), ('et', 'Estonian'), ('kok', 'Konkani'), ('sr-Latn', 'Serbian'), ('mk', 'Macedonian'), ('ks', 'Kashmiri'), ('as', 'Assamese'), ('uz', 'Uzbek'), ('am-et', 'Amharic'), ('sah', 'Sakha'), ('ka', 'Georgian'), ('nn-NO', 'Norwegian (Nynorsk)'), ('gu-IN', 'Gujarati (India)'), ('uk', 'Ukrainian'), ('de-DE', 'German (Germany)'), ('ln', 'Lingala'), ('mg', 'Malagasy'), ('gn', 'Guarani'), ('hsb', 'Upper Sorbian'), ('ca-valencia', 'Catalan (Valencian)'), ('es-CL', 'Spanish (Chile)'), ('lo', 'Lao'), ('or', 'Oriya'), ('ku', 'Kurdish'), ('nr', 'Ndebele, South'), ('es-ES', 'Spanish (Spain)'), ('kk', 'Kazakh'), ('nb-NO', 'Norwegian (Bokmål)'), ('he', 'Hebrew'), ('ast', 'Asturian'), ('ca', 'Catalan'), ('si', 'Sinhala'), ('tt-RU', 'Tatar'), ('fy-NL', 'Frisian'), ('la', 'Latin'), ('az', 'Azerbaijani'), ('nso', 'Northern Sotho'), ('el', 'Greek'), ('fi', 'Finnish'), ('csb', 'Kashubian'), ('sw', 'Swahili'), ('en-GB', 'English (British)'), ('eo', 'Esperanto'), ('mn', 'Mongolian'), ('sq', 'Albanian'), ('sv-SE', 'Swedish'), ('ff', 'Fulah'), ('tr', 'Turkish'), ('be', 'Belarusian'), ('mi', 'Maori (Aotearoa)'), ('cak', 'Kaqchikel'), ('gd', 'Gaelic (Scotland)'), ('ja', 'Japanese'), ('en-US', 'English (US)'), ('en-ZA', 'English (South African)'), ('en-CA', 'English (Canadian)'), ('tn', 'Tswana'), ('sl', 'Slovenian'), ('ta', 'Tamil'), ('pl', 'Polish'), ('hi-IN', 'Hindi (India)'), ('de-CH', 'German (Switzerland)'), ('cy', 'Welsh'), ('xh', 'Xhosa'), ('my', 'Burmese'), ('son', 'Songhai'), ('zh-TW', 'Chinese (Traditional)'), ('wo', 'Wolof'), ('rm', 'Romansh'), ('rw', 'Kinyarwanda'), ('pt-BR', 'Portuguese (Brazilian)'), ('cs', 'Czech'), ('pt-PT', 'Portuguese (Portugal)'), ('ta-IN', 'Tamil (India)'), ('zh-CN', 'Chinese (Simplified)'), ('sat', 'Santali'), ('ar', 'Arabic'), ('ha', 'Hausa'), ('ja-JP-mac', 'Japanese'), ('ga-IE', 'Irish'), ('ms', 'Malay'), ('tl', 'Tagalog'), ('ss', 'Siswati'), ('gu', 'Gujarati'), ('lt', 'Lithuanian'), ('fj-FJ', 'Fijian'), ('yo', 'Yoruba'), ('kn', 'Kannada'), ('x-testing', 'Testing'), ('an', 'Aragonese'), ('ach', 'Acholi'), ('mr', 'Marathi'), ('oc', 'Occitan (Lengadocian)'), ('eu', 'Basque'), ('ru', 'Russian'), ('sk', 'Slovak'), ('pa-IN', 'Punjabi (India)'), ('ve', 'Venda'), ('gl', 'Galician'), ('tsz', 'Purépecha'), ('pa', 'Punjabi'), ('ts', 'Tsonga'), ('en-NZ', 'English (New Zealand)'), ('fr', 'French'), ('es', 'Spanish'), ('ig', 'Igbo'), ('zu', 'Zulu'), ('ur', 'Urdu')], default='', max_length=255)),
                ('country', django_countries.fields.CountryField(default=None, max_length=2, null=True)),
                ('start_time', models.DateTimeField(default=None, null=True)),
                ('end_time', models.DateTimeField(default=None, null=True)),
                ('sample_rate', PercentField(default=100)),
            ],
        ),
    ]
