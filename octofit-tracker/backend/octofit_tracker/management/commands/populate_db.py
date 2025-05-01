from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Conectar ao MongoDB
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

        # Limpar coleções existentes
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Criar usuários
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)

        # Criar times
        teams = [
            {"_id": ObjectId(), "name": "Blue Team", "members": [users[0]["_id"], users[1]["_id"], users[2]["_id"]]},
            {"_id": ObjectId(), "name": "Gold Team", "members": [users[3]["_id"], users[4]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Criar atividades
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Cycling", "duration": 60, "date": "2024-05-01T10:00:00Z"},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Crossfit", "duration": 120, "date": "2024-05-01T11:00:00Z"},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Running", "duration": 90, "date": "2024-05-01T12:00:00Z"},
            {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "Strength", "duration": 30, "date": "2024-05-01T13:00:00Z"},
            {"_id": ObjectId(), "user": users[4]["_id"], "activity_type": "Swimming", "duration": 75, "date": "2024-05-01T14:00:00Z"},
        ]
        db.activity.insert_many(activities)

        # Criar leaderboard
        leaderboard = [
            {"_id": ObjectId(), "user": users[0]["_id"], "points": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "points": 90},
            {"_id": ObjectId(), "user": users[2]["_id"], "points": 95},
            {"_id": ObjectId(), "user": users[3]["_id"], "points": 85},
            {"_id": ObjectId(), "user": users[4]["_id"], "points": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Criar treinos
        workouts = [
            {"_id": ObjectId(), "user": users[0]["_id"], "workout_type": "Cycling Training", "details": "Training for a road cycling event", "date": "2024-05-01T15:00:00Z"},
            {"_id": ObjectId(), "user": users[1]["_id"], "workout_type": "Crossfit", "details": "Training for a crossfit competition", "date": "2024-05-01T16:00:00Z"},
            {"_id": ObjectId(), "user": users[2]["_id"], "workout_type": "Running Training", "details": "Training for a marathon", "date": "2024-05-01T17:00:00Z"},
            {"_id": ObjectId(), "user": users[3]["_id"], "workout_type": "Strength Training", "details": "Training for strength", "date": "2024-05-01T18:00:00Z"},
            {"_id": ObjectId(), "user": users[4]["_id"], "workout_type": "Swimming Training", "details": "Training for a swimming competition", "date": "2024-05-01T19:00:00Z"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
