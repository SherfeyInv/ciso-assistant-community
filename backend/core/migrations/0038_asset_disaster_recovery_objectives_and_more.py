# Generated by Django 5.1.1 on 2024-11-22 07:00

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0037_appliedcontrol_priority"),
    ]

    operations = [
        migrations.AddField(
            model_name="asset",
            name="disaster_recovery_objectives",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="The disaster recovery objectives of the asset",
                validators=[
                    core.validators.JSONSchemaInstanceValidator(
                        {
                            "$id": "https://ciso-assistant.com/schemas/assets/security_objectives.schema.json",
                            "$schema": "https://json-schema.org/draft/2020-12/schema",
                            "description": "The security objectives of the asset",
                            "properties": {
                                "objectives": {
                                    "patternProperties": {
                                        "^[a-z_]+$": {
                                            "properties": {
                                                "value": {
                                                    "minimum": 0,
                                                    "type": "integer",
                                                }
                                            },
                                            "type": "object",
                                        }
                                    },
                                    "type": "object",
                                }
                            },
                            "title": "Security objectives",
                            "type": "object",
                        }
                    )
                ],
                verbose_name="Disaster recovery objectives",
            ),
        ),
        migrations.AddField(
            model_name="asset",
            name="reference_link",
            field=models.URLField(
                blank=True,
                help_text="External url for action follow-up (eg. Jira ticket)",
                max_length=2048,
                null=True,
                verbose_name="Link",
            ),
        ),
        migrations.AddField(
            model_name="asset",
            name="security_objectives",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="The security objectives of the asset",
                validators=[
                    core.validators.JSONSchemaInstanceValidator(
                        {
                            "$id": "https://ciso-assistant.com/schemas/assets/security_objectives.schema.json",
                            "$schema": "https://json-schema.org/draft/2020-12/schema",
                            "description": "The security objectives of the asset",
                            "properties": {
                                "objectives": {
                                    "patternProperties": {
                                        "^[a-z_]+$": {
                                            "properties": {
                                                "is_enabled": {"type": "boolean"},
                                                "value": {
                                                    "minimum": 0,
                                                    "type": "integer",
                                                },
                                            },
                                            "type": "object",
                                        }
                                    },
                                    "type": "object",
                                }
                            },
                            "title": "Security objectives",
                            "type": "object",
                        }
                    )
                ],
                verbose_name="Security objectives",
            ),
        ),
    ]
