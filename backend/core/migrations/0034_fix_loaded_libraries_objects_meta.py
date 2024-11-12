# Generated by Django 5.1 on 2024-11-07 12:10

from django.db import migrations


def fix_libraries_objects_meta(apps, schema_editor):
    LoadedLibrary = apps.get_model("core", "LoadedLibrary")

    for library in LoadedLibrary.objects.all():
        objects_meta = library.objects_meta
        if "frameworks" in objects_meta:
            objects_meta["framework"] = objects_meta.pop("frameworks")
            library.save()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0033_fix_mitre_lib_version"),
    ]

    operations = [migrations.RunPython(fix_libraries_objects_meta)]
