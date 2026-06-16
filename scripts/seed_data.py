import random

from data.database import SessionLocal
from data.models import (
    User,
    Content,
    Skill,
    UserSkill,
    ContentSkill,
    Interaction
)

db = SessionLocal()

# -------------------------
# Clear Existing Data
# -------------------------

db.query(Interaction).delete()
db.query(ContentSkill).delete()
db.query(UserSkill).delete()
db.query(Content).delete()
db.query(Skill).delete()
db.query(User).delete()

db.commit()

# -------------------------
# Skills
# -------------------------

skill_names = [
    "Python",
    "SQL",
    "Machine Learning",
    "Data Science",
    "Deep Learning",
    "Statistics",
    "Java",
    "Web Development"
]

skills = []

for name in skill_names:
    skill = Skill(name=name)
    db.add(skill)
    skills.append(skill)

db.commit()

skills = db.query(Skill).all()

# -------------------------
# Users
# -------------------------

users = [
    User(name="Alice", interests="Python,ML"),
    User(name="Bob", interests="SQL,Data Science"),
    User(name="Charlie", interests="Java"),
    User(name="David", interests="Statistics"),
    User(name="Emma", interests="Deep Learning"),
    User(name="Frank", interests="Python"),
    User(name="Grace", interests="Web Development"),
    User(name="Helen", interests="Machine Learning"),
    User(name="Ivan", interests="SQL"),
    User(name="Jack", interests="Data Science")
]

db.add_all(users)
db.commit()

users = db.query(User).all()

# -------------------------
# Content
# -------------------------

contents = []

for i in range(1, 21):

    content = Content(
        title=f"Course {i}",
        category=random.choice([
            "Programming",
            "AI",
            "Database",
            "Web"
        ]),
        difficulty=random.choice([
            "Beginner",
            "Intermediate",
            "Advanced"
        ]),
        popularity=random.uniform(1, 10)
    )

    contents.append(content)

db.add_all(contents)
db.commit()

contents = db.query(Content).all()

# -------------------------
# User Skills
# -------------------------

for user in users:

    selected_skills = random.sample(
        skills,
        random.randint(2, 4)
    )

    for skill in selected_skills:

        db.add(
            UserSkill(
                user_id=user.id,
                skill_id=skill.id,
                proficiency=round(
                    random.uniform(0.5, 1.0),
                    2
                )
            )
        )

db.commit()

# -------------------------
# Content Skills
# -------------------------

for content in contents:

    selected_skills = random.sample(
        skills,
        random.randint(1, 3)
    )

    for skill in selected_skills:

        db.add(
            ContentSkill(
                content_id=content.id,
                skill_id=skill.id
            )
        )

db.commit()

# -------------------------
# Interactions
# -------------------------

for _ in range(100):

    db.add(
        Interaction(
            user_id=random.choice(users).id,
            content_id=random.choice(contents).id,
            type=random.choice([
                "view",
                "click",
                "like",
                "rating"
            ]),
            rating=random.randint(1, 5)
        )
    )

db.commit()

print("Database seeded successfully!")