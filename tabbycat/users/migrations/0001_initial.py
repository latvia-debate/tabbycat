# Generated by Django 5.0.4 on 2024-05-12 17:19

import django.db.models.deletion
import utils.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("tournaments", "0010_alter_round_draw_type"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="name")),
                (
                    "permissions",
                    utils.fields.ChoiceArrayField(
                        base_field=models.CharField(
                            choices=[
                                (
                                    "view.adjudicatorteamconflict",
                                    "view adjudicator-team conflicts",
                                ),
                                (
                                    "edit.adjudicatorteamconflict",
                                    "edit adjudicator-team conflicts",
                                ),
                                (
                                    "view.adjudicatoradjudicatorconflict",
                                    "view adjudicator-adjudicator conflicts",
                                ),
                                (
                                    "edit.adjudicatoradjudicatorconflict",
                                    "edit adjudicator-adjudicator conflicts",
                                ),
                                (
                                    "view.adjudicatorinstitutionconflict",
                                    "view adjudicator-institution conflicts",
                                ),
                                (
                                    "edit.adjudicatorinstitutionconflict",
                                    "edit adjudicator-institution conflicts",
                                ),
                                (
                                    "view.teaminstitutionconflict",
                                    "view team-institution conflicts",
                                ),
                                (
                                    "edit.teaminstitutionconflict",
                                    "edit team-institution conflicts",
                                ),
                                ("view.actionlogentry", "view action log entries"),
                                ("view.team", "view teams"),
                                ("add.team", "add teams"),
                                ("view.teamname", "view decoded team names"),
                                (
                                    "view.anonymous",
                                    "View names of anonymized participants",
                                ),
                                ("view.adj", "view adjudicators"),
                                ("add.adj", "add adjudicators"),
                                ("view.room", "view rooms"),
                                ("add.room", "add rooms"),
                                ("view.inst", "view institutions"),
                                ("add.inst", "add institutions"),
                                ("view.particpants", "view participants"),
                                (
                                    "view.participants.gender",
                                    "view participants' gender information",
                                ),
                                (
                                    "view.participants.contact",
                                    "view participants' contact information",
                                ),
                                (
                                    "view.participants.decoded",
                                    "view participants' real names",
                                ),
                                (
                                    "view.participants.inst",
                                    "view participants' institution",
                                ),
                                (
                                    "view.roundavailability.team",
                                    "view round availabilities for teams",
                                ),
                                (
                                    "view.roundavailability.adjudicator",
                                    "view round availabilities for adjudicators",
                                ),
                                (
                                    "view.roundavailability.venue",
                                    "view round availabilities for rooms",
                                ),
                                (
                                    "edit.roundavailability.team",
                                    "edit round availabilities for teams",
                                ),
                                (
                                    "edit.roundavailability.adjudicator",
                                    "edit round availabilities for adjudicators",
                                ),
                                (
                                    "edit.roundavailability.venue",
                                    "edit round availabilities for rooms",
                                ),
                                ("view.roundavailability", "view round availabilities"),
                                ("edit.roundavailability", "edit round availabilities"),
                                ("view.roomconstraints", "view room constraints"),
                                ("view.roomcategories", "view room categories"),
                                ("edit.roomconstraints", "edit room constraints"),
                                ("edit.roomcategories", "edit room categories"),
                                ("view.debate", "view debates (draw)"),
                                ("view.debate.admin", "view debates (detailed draw)"),
                                ("generate.debate", "generate debates (draw)"),
                                ("edit.debateteam", "edit debate teams (pairings)"),
                                (
                                    "view.debateadjudicator",
                                    "view debate adjudicators (allocations)",
                                ),
                                (
                                    "edit.debateadjudicator",
                                    "edit debate adjudicators (allocations)",
                                ),
                                ("view.roomallocations", "view room allocations"),
                                ("edit.roomallocations", "edit room allocations"),
                                (
                                    "edit.allocatesides",
                                    "edit and confirm outround team positions",
                                ),
                                ("view.ballotsubmission.new", "view confirmed ballots"),
                                (
                                    "edit.ballotsubmission.old",
                                    "edit non-confirmed ballots",
                                ),
                                ("view.ballotsubmission", "view any ballot"),
                                ("edit.ballotsubmission", "edit any ballot"),
                                ("add.ballotsubmission", "create ballots"),
                                ("mark.ballotsubmission", "confirm/discard any ballot"),
                                (
                                    "mark.ballotsubmission.others",
                                    "confirm/discard others' ballots",
                                ),
                                ("view.ballotsubmission.graph", "view ballot graph"),
                                ("view.results", "view results entry page"),
                                ("view.roundmotion", "view motion per round"),
                                ("edit.roundmotion", "edit motion per round"),
                                ("release.draw", "release draw to public"),
                                ("release.motion", "release motion to public"),
                                ("unrelease.draw", "unrelease draw to public"),
                                ("unrelease.motion", "unrelease motion to public"),
                                ("edit.starttime", "add debate start time"),
                                ("view.draw", "view draws"),
                                (
                                    "view.briefingdraw",
                                    "view draws (for the briefing room)",
                                ),
                                (
                                    "display.motion",
                                    "display motion (for the briefing room)",
                                ),
                                (
                                    "view.tournamentpreferencemodel",
                                    "view tournament configuration",
                                ),
                                (
                                    "edit.tournamentpreferencemodel",
                                    "edit tournament configuration",
                                ),
                                (
                                    "view.preformedpanels",
                                    "view existing preformed panels",
                                ),
                                ("edit.preformedpanels", "edit preformed panels"),
                                (
                                    "view.standingsoverview",
                                    "view the overviews of standings",
                                ),
                                (
                                    "view.teamstandings",
                                    "view the most recent team standings",
                                ),
                                (
                                    "view.speakersstandings",
                                    "view the most recent speaker standings",
                                ),
                                (
                                    "view.repliesstandings",
                                    "view the most recent replies standings",
                                ),
                                ("view.motionstab", "view the most recent motions tab"),
                                ("view.diversitytab", "view the diversity tab"),
                                (
                                    "view.feedbackoverview",
                                    "view overview of judge feedback",
                                ),
                                ("edit.judgescoresbulk", "bulk update judge scores"),
                                ("edit.judgescoresind", "edit base scores of judges"),
                                ("view.feedback", "view feedback"),
                                ("edit.feedbackignore", "toggle ignore feedback"),
                                ("edit.feedbackconfirm", "toggle confirm feedback"),
                                (
                                    "view.feedbackunsubmitted",
                                    "view feedback unsubmitted tab",
                                ),
                                ("add.feedback", "add feedback"),
                                ("view.adj.break", "view adjudicator break"),
                                ("edit.adj.break", "edit adjudicator break"),
                                ("edit.feedbackquestion", "edit feedback questions"),
                                ("edit.breakeligibility", "edit break eligibility"),
                                ("view.breakeligibility", "view break eligibility"),
                                ("edit.breakcategories", "edit break categories"),
                                ("view.breakcategories", "view break categories"),
                                ("view.speakercategories", "view speaker categories"),
                                ("edit.speakercategories", "edit speaker categories"),
                                ("view.speakereligibility", "view speaker eligibility"),
                                ("edit.speakereligibility", "edit speaker eligibility"),
                                ("view.break.overview", "view break overview"),
                                ("view.break", "view breaks"),
                                ("generate.break", "generate all breaks"),
                                ("view.privateurls", "view private urls"),
                                (
                                    "view.privateurls.emaillist",
                                    "view private urls email list",
                                ),
                                ("generate.privateurls", "generate private URLs"),
                                ("send.privateurls", "send private URLs"),
                                ("view.checkin", "view checkins"),
                                (
                                    "edit.participantcheckin",
                                    "edit participant check-in",
                                ),
                                ("edit.roomcheckin", "edit room check-in"),
                                ("edit.round", "edit round attributes"),
                                ("delete.round", "delete rounds"),
                                ("add.round", "create rounds"),
                                ("view.emails", "view email statuses"),
                                ("send.emails", "send participants email messages"),
                                ("export.xml", "export DebateXML"),
                                ("view.settings", "view settings"),
                                ("edit.settings", "edit settings"),
                            ],
                            max_length=50,
                        ),
                        blank=True,
                        default=list,
                        size=None,
                        verbose_name="permissions",
                    ),
                ),
                (
                    "tournament",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tournaments.tournament",
                        verbose_name="tournament",
                    ),
                ),
            ],
            options={
                "verbose_name": "group",
                "verbose_name_plural": "groups",
                "unique_together": {("name", "tournament")},
            },
        ),
        migrations.CreateModel(
            name="Membership",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.group",
                        verbose_name="group",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "group membership",
                "verbose_name_plural": "group memberships",
                "unique_together": {("user", "group")},
            },
        ),
        migrations.CreateModel(
            name="UserPermission",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "permission",
                    models.CharField(
                        choices=[
                            (
                                "view.adjudicatorteamconflict",
                                "view adjudicator-team conflicts",
                            ),
                            (
                                "edit.adjudicatorteamconflict",
                                "edit adjudicator-team conflicts",
                            ),
                            (
                                "view.adjudicatoradjudicatorconflict",
                                "view adjudicator-adjudicator conflicts",
                            ),
                            (
                                "edit.adjudicatoradjudicatorconflict",
                                "edit adjudicator-adjudicator conflicts",
                            ),
                            (
                                "view.adjudicatorinstitutionconflict",
                                "view adjudicator-institution conflicts",
                            ),
                            (
                                "edit.adjudicatorinstitutionconflict",
                                "edit adjudicator-institution conflicts",
                            ),
                            (
                                "view.teaminstitutionconflict",
                                "view team-institution conflicts",
                            ),
                            (
                                "edit.teaminstitutionconflict",
                                "edit team-institution conflicts",
                            ),
                            ("view.actionlogentry", "view action log entries"),
                            ("view.team", "view teams"),
                            ("add.team", "add teams"),
                            ("view.teamname", "view decoded team names"),
                            ("view.anonymous", "View names of anonymized participants"),
                            ("view.adj", "view adjudicators"),
                            ("add.adj", "add adjudicators"),
                            ("view.room", "view rooms"),
                            ("add.room", "add rooms"),
                            ("view.inst", "view institutions"),
                            ("add.inst", "add institutions"),
                            ("view.particpants", "view participants"),
                            (
                                "view.participants.gender",
                                "view participants' gender information",
                            ),
                            (
                                "view.participants.contact",
                                "view participants' contact information",
                            ),
                            (
                                "view.participants.decoded",
                                "view participants' real names",
                            ),
                            (
                                "view.participants.inst",
                                "view participants' institution",
                            ),
                            (
                                "view.roundavailability.team",
                                "view round availabilities for teams",
                            ),
                            (
                                "view.roundavailability.adjudicator",
                                "view round availabilities for adjudicators",
                            ),
                            (
                                "view.roundavailability.venue",
                                "view round availabilities for rooms",
                            ),
                            (
                                "edit.roundavailability.team",
                                "edit round availabilities for teams",
                            ),
                            (
                                "edit.roundavailability.adjudicator",
                                "edit round availabilities for adjudicators",
                            ),
                            (
                                "edit.roundavailability.venue",
                                "edit round availabilities for rooms",
                            ),
                            ("view.roundavailability", "view round availabilities"),
                            ("edit.roundavailability", "edit round availabilities"),
                            ("view.roomconstraints", "view room constraints"),
                            ("view.roomcategories", "view room categories"),
                            ("edit.roomconstraints", "edit room constraints"),
                            ("edit.roomcategories", "edit room categories"),
                            ("view.debate", "view debates (draw)"),
                            ("view.debate.admin", "view debates (detailed draw)"),
                            ("generate.debate", "generate debates (draw)"),
                            ("edit.debateteam", "edit debate teams (pairings)"),
                            (
                                "view.debateadjudicator",
                                "view debate adjudicators (allocations)",
                            ),
                            (
                                "edit.debateadjudicator",
                                "edit debate adjudicators (allocations)",
                            ),
                            ("view.roomallocations", "view room allocations"),
                            ("edit.roomallocations", "edit room allocations"),
                            (
                                "edit.allocatesides",
                                "edit and confirm outround team positions",
                            ),
                            ("view.ballotsubmission.new", "view confirmed ballots"),
                            ("edit.ballotsubmission.old", "edit non-confirmed ballots"),
                            ("view.ballotsubmission", "view any ballot"),
                            ("edit.ballotsubmission", "edit any ballot"),
                            ("add.ballotsubmission", "create ballots"),
                            ("mark.ballotsubmission", "confirm/discard any ballot"),
                            (
                                "mark.ballotsubmission.others",
                                "confirm/discard others' ballots",
                            ),
                            ("view.ballotsubmission.graph", "view ballot graph"),
                            ("view.results", "view results entry page"),
                            ("view.roundmotion", "view motion per round"),
                            ("edit.roundmotion", "edit motion per round"),
                            ("release.draw", "release draw to public"),
                            ("release.motion", "release motion to public"),
                            ("unrelease.draw", "unrelease draw to public"),
                            ("unrelease.motion", "unrelease motion to public"),
                            ("edit.starttime", "add debate start time"),
                            ("view.draw", "view draws"),
                            ("view.briefingdraw", "view draws (for the briefing room)"),
                            (
                                "display.motion",
                                "display motion (for the briefing room)",
                            ),
                            (
                                "view.tournamentpreferencemodel",
                                "view tournament configuration",
                            ),
                            (
                                "edit.tournamentpreferencemodel",
                                "edit tournament configuration",
                            ),
                            ("view.preformedpanels", "view existing preformed panels"),
                            ("edit.preformedpanels", "edit preformed panels"),
                            (
                                "view.standingsoverview",
                                "view the overviews of standings",
                            ),
                            (
                                "view.teamstandings",
                                "view the most recent team standings",
                            ),
                            (
                                "view.speakersstandings",
                                "view the most recent speaker standings",
                            ),
                            (
                                "view.repliesstandings",
                                "view the most recent replies standings",
                            ),
                            ("view.motionstab", "view the most recent motions tab"),
                            ("view.diversitytab", "view the diversity tab"),
                            (
                                "view.feedbackoverview",
                                "view overview of judge feedback",
                            ),
                            ("edit.judgescoresbulk", "bulk update judge scores"),
                            ("edit.judgescoresind", "edit base scores of judges"),
                            ("view.feedback", "view feedback"),
                            ("edit.feedbackignore", "toggle ignore feedback"),
                            ("edit.feedbackconfirm", "toggle confirm feedback"),
                            (
                                "view.feedbackunsubmitted",
                                "view feedback unsubmitted tab",
                            ),
                            ("add.feedback", "add feedback"),
                            ("view.adj.break", "view adjudicator break"),
                            ("edit.adj.break", "edit adjudicator break"),
                            ("edit.feedbackquestion", "edit feedback questions"),
                            ("edit.breakeligibility", "edit break eligibility"),
                            ("view.breakeligibility", "view break eligibility"),
                            ("edit.breakcategories", "edit break categories"),
                            ("view.breakcategories", "view break categories"),
                            ("view.speakercategories", "view speaker categories"),
                            ("edit.speakercategories", "edit speaker categories"),
                            ("view.speakereligibility", "view speaker eligibility"),
                            ("edit.speakereligibility", "edit speaker eligibility"),
                            ("view.break.overview", "view break overview"),
                            ("view.break", "view breaks"),
                            ("generate.break", "generate all breaks"),
                            ("view.privateurls", "view private urls"),
                            (
                                "view.privateurls.emaillist",
                                "view private urls email list",
                            ),
                            ("generate.privateurls", "generate private URLs"),
                            ("send.privateurls", "send private URLs"),
                            ("view.checkin", "view checkins"),
                            ("edit.participantcheckin", "edit participant check-in"),
                            ("edit.roomcheckin", "edit room check-in"),
                            ("edit.round", "edit round attributes"),
                            ("delete.round", "delete rounds"),
                            ("add.round", "create rounds"),
                            ("view.emails", "view email statuses"),
                            ("send.emails", "send participants email messages"),
                            ("export.xml", "export DebateXML"),
                            ("view.settings", "view settings"),
                            ("edit.settings", "edit settings"),
                        ],
                        max_length=50,
                        verbose_name="permission",
                    ),
                ),
                (
                    "tournament",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tournaments.tournament",
                        verbose_name="tournament",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "user permission",
                "verbose_name_plural": "user permissions",
                "unique_together": {("user", "permission", "tournament")},
            },
        ),
    ]
