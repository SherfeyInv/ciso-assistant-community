# Generated by Django 5.0.4 on 2024-05-22 17:31

from django.db import migrations


def fix_urns_for_enisa_5g_scm(apps, schema_editor):
    StoredLibrary = apps.get_model("core", "StoredLibrary")
    LoadedLibrary = apps.get_model("core", "LoadedLibrary")
    enisa_5g_scm_stored_library = StoredLibrary.objects.filter(
        urn="urn:intuitem:risk:library:enisa-5g-scm-v1.3"
    )
    if enisa_5g_scm_stored_library:
        enisa_5g_scm_stored_library[
            0
        ].delete()  # the lib will be added again in the store at the end of the migration
    enisa_5g_scm_loaded_library = LoadedLibrary.objects.filter(
        urn="urn:intuitem:risk:library:enisa-5g-scm-v1.3"
    )
    if enisa_5g_scm_loaded_library:
        count = 0
        for b in enisa_5g_scm_loaded_library[0].reference_controls.all():
            if b.urn[:4] != "urn:":
                b.urn = "urn:intuitem:" + b.urn
                b.save()
                count += 1
        print(f"fixed {count} URNs")


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0013_requirementnode_typical_evidence"),
    ]

    operations = [
        migrations.RunPython(fix_urns_for_enisa_5g_scm),
    ]
